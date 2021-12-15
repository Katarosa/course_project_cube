from sqlalchemy import (
    Column,
    Integer,
    String,
    LargeBinary,
    Boolean,
    DateTime,
    ForeignKey,
    Float,
    Table,
    Enum
)

from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

from db import Base


class Buildings(Enum):
    b1dot1 = 0
    b1dot2 = 1
    #so on


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    password = Column(LargeBinary)
    salt = Column(LargeBinary)
    phone = Column(String, unique=True)
    email = Column(String, unique=True)
    building = Column(Buildings)
