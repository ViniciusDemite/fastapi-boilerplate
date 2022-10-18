from http.client import HTTPException
from typing import Union
from fastapi import status
from typing import List
from sqlalchemy.orm import Session
from ..models import users as model
from ..schemas import users as schema
from .encrypt import hash_password


def get_user_by_id(db: Session, user_id: int) -> Union[schema.User, None]:
  return db.query(model.User).filter(model.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> Union[schema.User, None]:
  return db.query(model.User).filter(model.User.email == email).first()


def get_user_by_username(db: Session, username: str) -> Union[schema.User, None]:
  return db.query(model.User).filter(model.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[schema.User]:
  return db.query(model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schema.UserCreate) -> schema.User:
  db_user = model.User(
    full_name=user.full_name,
    username=user.username,
    email=user.email,
    hashed_password=hash_password(user.password)
  )

  db.add(db_user)
  db.commit()
  db.refresh(db_user)

  return db_user


def update_user(db: Session, user: schema.UserUpdate, user_id: int) -> schema.User:
  db_user = get_user_by_id(db, user_id)

  for var, value in vars(user).items():
    if value is not None:
      setattr(db_user, var, value)

  if user.password is not None:
    if user.confirm_password is None:
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        details="Please confirm your password"
      )

    if user.password != user.confirm_password:
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        details="Passwords do not match"
      )

    db_user.hashed_password = hash_password(user.password)

  db.add(db_user)
  db.commit()
  db.refresh(db_user)

  return db_user


def delete_user(db: Session, user_id: int) -> schema.User:
  db_user = get_user_by_id(db, user_id)

  db.delete(db_user)
  db.commit()

  return db_user