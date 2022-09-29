from sqlalchemy import Column, String, Boolean, Integer

from ..database import Base


class UserAdmin(Base):

    __tablename__ = "user_admin"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    is_admin = Column(Boolean, default=False)
