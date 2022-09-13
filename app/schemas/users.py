from typing import Union
from pydantic import BaseModel


class UserBase(BaseModel):
  name: str
  email: str

class UserCreate(UserBase):
  password: str
  confirm_password: str

class UserUpdate(UserBase):
  password: Union[str, None] = None
  confirm_password: Union[str, None] = None

class User(UserBase):
  id: int