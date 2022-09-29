"""Models module."""

from sqlalchemy import Column, String, Boolean, Integer

from .database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)
    


class UserAdmin(Base):

    __tablename__ = "user_admin"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    is_admin = Column(Boolean, default=False)
    

class UserReport(Base):

    __tablename__ = "user_report"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    data = Column(String)
    
