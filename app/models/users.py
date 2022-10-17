from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from ..config.database import Base


class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, index=True)
  full_name = Column(String(255))
  username = Column(String(50), unique=True)
  email = Column(String(100), unique=True)
  hashed_password = Column(String(255))
  is_active = Column(Boolean, default=True)
  created_at = Column(DateTime(timezone=True), default=func.now())
  updated_at = Column(DateTime(timezone=True), nullable=True, default=None, onupdate=func.now())