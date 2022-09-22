from typing import List
from sqlalchemy.orm import Session
from ..models import users as model
from ..schemas import users as schema
from .encrypt import hash_password


def get_user_by_id(db: Session, user_id: int) -> schema.User:
  return db.query(model.User).filter(model.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> schema.User:
  return db.query(model.User).filter(model.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[schema.User]:
  return db.query(model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schema.UserCreate) -> schema.User:
  db_user = model.User(
    name=user.name,
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
    setattr(db_user, var, value) if value else None

  if user.password:
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