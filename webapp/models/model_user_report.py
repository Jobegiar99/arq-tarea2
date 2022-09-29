from sqlalchemy import Column, String, Boolean, Integer

from ..database import Base


class UserReport(Base):

    __tablename__ = "user_report"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    data = Column(String)
