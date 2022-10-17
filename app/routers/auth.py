import os
from typing import Union
from datetime import timedelta, datetime
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import jwt
from ..schemas.users import User
from ..utils.user_crud import get_user_by_username
from ..utils.encrypt import verify_password
from ..dependencies.general import get_db
from ..schemas.auth import Token


router = APIRouter(
  tags=['auth']
)

def authenticate_user(username: str, password: str, db: Session) -> Union[User, None]:
  """Autentica um usuário por email e senha

  Args:
      user_email (str): email utilizado pelo usuário
      password (str): senha do usuário
      db (Session): sessão do banco de dados

  Returns:
      Union[User, None]: dados do usuário caso exista no banco de dados, se não None para informar que o usuário não foi encontrado na base de dados.
  """
  db_user = get_user_by_username(db, username)

  if not db_user or not verify_password(password, db_user.hashed_password):
    return None

  return db_user

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None) -> str:
  """Cria um token de acesso para o usuário ao logar com as informações corretas.

  Args:
      data (dict): _description_
      expires_delta (Union[timedelta, None], optional): intervalo de tempo para a expiração do token. Defaults to None.

  Returns:
      str: token codificado
  """
  to_encode = data.copy()
  expire = datetime.utcnow() + timedelta(minutes=15) if not expires_delta else \
  datetime.utcnow() + expires_delta

  to_encode.update({"exp": expire})

  encoded_jwt = jwt.encode(
    claims=to_encode,
    key=os.getenv('JWT_SECRET_KEY'),
    algorithm=os.getenv('HASH_ALGORITHM')
  )

  return encoded_jwt

@router.post('/token', response_model=Token)
async def login_for_access_token(
  form_data: OAuth2PasswordRequestForm = Depends(),
  db: Session = Depends(get_db)
  ) -> Token:
  """Recebe os dados do usuário por um formulário e libera acesso por token, se verificado corretamente.

  Args:
      form_data (OAuth2PasswordRequestForm, optional): campos do formulário de login. Defaults to Depends().
      db (Session, optional): sessão do banco de dados. Defaults to Depends(get_db).

  Raises:
      HTTPException: retorna um código 401 informando que as credenciais do usuário não estão de acordo com o banco de dados.

  Returns:
      Token: objeto com o token de autenticação e seu tipo
  """
  user = authenticate_user(form_data.username, form_data.password, db)

  if not user:
    raise HTTPException(
      status_code=401,
      detail='Incorrect username or password!',
      headers={"WWW-Authenticate": "Bearer"}
    )

  access_token_expire = timedelta(
    minutes=int(os.getenv('ACCESS_TOKEN_EXPIRATION_MINUTES'))
  )
  access_token = create_access_token({"sub": user.username}, access_token_expire)

  return {
    "access_token": access_token,
    "token_type": 'bearer'
  }