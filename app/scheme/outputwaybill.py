from pydantic import BaseModel
from app.base.outputwaybillbase import Status


class OutputWaybillBase(BaseModel):
    number: int


class OutputWaybillCreate(OutputWaybillBase):
    pass


class OutputWaybillUpdate(OutputWaybillBase):
    status: Status


class OutputWaybill(OutputWaybillBase):
    id: int
    status: Status

    class Config:
        orm_mode = True
