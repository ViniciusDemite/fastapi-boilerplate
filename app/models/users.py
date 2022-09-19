from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from ..config.database import Base


class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, nullable=False, index=True)
  name = Column(String(50), nullable=False)
  email = Column(String(100), unique=True)
  hashed_password = Column(String(255), nullable=False)
  is_active = Column(Boolean, nullable=False, default=True)
  created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
  updated_at = Column(DateTime(timezone=True), nullable=False, onupdate=func.utcnow())