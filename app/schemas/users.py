from typing import Union
from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
  name: str
  email: str

class UserCreate(UserBase):
  password: str
  confirm_password: str

class UserUpdate(UserBase):
  is_active: Union[bool, None] = None
  password: Union[str, None] = None
  confirm_password: Union[str, None] = None

class User(UserBase):
  id: int
  is_active: bool
  created_at: datetime
  updated_at: Union[datetime, None]

  class Config:
    orm_mode = True