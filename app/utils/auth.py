from os import getenv
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from ..schemas.auth import TokenData
from ..schemas.users import User
from sqlalchemy.orm import Session
from ..dependencies.general import get_db
from ..utils.user_crud import get_user_by_username


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
  credentials_exception = HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Could not validate credentials",
      headers={"WWW-Authenticate": "Bearer"},
  )

  try:
      payload = jwt.decode(
        token,
        getenv('JWT_SECRET_KEY'),
        algorithms=[getenv('HASH_ALGORITHM')]
      )
      username: str = payload.get("sub")

      if username is None:
          raise credentials_exception

      token_data = TokenData(username=username)
  except JWTError:
      raise credentials_exception

  user = get_user_by_username(db, token_data.username)

  if user is None:
      raise credentials_exception

  return user


async def get_active_user(user: User = Depends(get_current_user)) -> User:
  if not user.is_active:
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail="Inactive user"
    )

  return user