from sqlalchemy import Column, Integer, Enum
import enum
from sqlalchemy.orm import declarative_base

Base_iw = declarative_base()


class Status(enum.Enum):
    CREATED = "CREATED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class InputWaybillBase(Base_iw):
    __tablename__ = "Inputwaybill"
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    status = Column(Enum(Status))

    def __init__(self, number, status):
        self.number = number
        self.status = status

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.id, self.number, self.status)
