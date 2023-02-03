from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from api.database import Base


class User(Base):
    """ SQLAlchemy model for users """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first = Column(String)
    last = Column(String)


class Bug(Base):
    """ SQLAlchemy model for bugs """
    __tablename__ = "bugs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    is_open = Column(Boolean, default=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
