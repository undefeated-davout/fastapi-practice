from app.utils.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from .timestamp_base import TimestampBase


class UserModel(Base, TimestampBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256))
    email = Column(String(256))
    password = Column(String(256))
    blogs = relationship("BlogModel", back_populates="creator")
