from typing import Union
from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
  full_name: str
  username: str
  email: str

class UserUpdate(BaseModel):
  full_name: Union[str, None] = None
  username: Union[str, None] = None
  email: Union[str, None] = None
  is_active: Union[bool, None] = None
  password: Union[str, None] = None
  confirm_password: Union[str, None] = None

class UserCreate(UserBase):
  password: str
  confirm_password: str

class User(UserBase):
  id: int
  is_active: bool
  created_at: datetime
  updated_at: Union[datetime, None]

  class Config:
    orm_mode = True