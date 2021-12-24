from app.utils.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from .timestamp_base import TimestampBase


class BlogModel(Base, TimestampBase):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    body = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("UserModel", back_populates="blogs")
