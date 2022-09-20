from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.users import User, UserCreate, UserUpdate
from ..dependencies.general import get_db
from ..utils import user_crud as crud


router = APIRouter(
  prefix='/users',
  tags=['users']
)

@router.get('/', response_model=List[User])
def list_users(db: Session = Depends(get_db)):
  """# Lista todos os usuários existentes.

  O parâmetro query é utilizado para fazer o filtro de usuários.
  """
  return crud.get_users(db)

@router.get('/{user_id}', response_model=User)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
  """# Pega os dados de um usuário específico"""
  db_user = crud.get_user_by_id(db, user_id)

  if db_user is None:
    raise HTTPException(status_code=404, detail="User not found!")

  return db_user

@router.post('/', response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
  """# Cria uma usuário de acordo com os dados passados.
  
  O parâmetro user é um schema com base nos dados a serem recebidos.
  """
  if user.password != user.confirm_password:
    raise HTTPException(status_code=400, detail="Passwords do not match!")

  db_user = crud.get_user_by_email(db, user.email)

  if db_user:
    raise HTTPException(status_code=400, detail="Email already registered!")

  return crud.create_user(db, user)

@router.put('/{user_id}', response_model=User)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
  """# Atualiza as informações do usuário de acordo com os dados passados.
  
  O parâmetro user é um schema com base nos dados a serem recebidos.
  """
  if user.password and user.password != user.confirm_password:
    raise HTTPException(status_code=400, detail="Passwords do not match!")

  updated_user = crud.update_user(db, user, user_id)

  return updated_user

@router.delete('/{user_id}', response_model=User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
  """# Apaga usuário e dados relacionados.

  ## Parâmetros:

  - **user_id** é utilizado para achar o usuário no banco de dados.
  - **db** é utilizado para a conexão com o banco de dados
  """
  return crud.delete_user(db, user_id)