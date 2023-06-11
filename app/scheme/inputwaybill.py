from pydantic import BaseModel
from app.base.inputwaybillbase import Status


class InputWaybillBase(BaseModel):
    number: int


class InputWaybillCreate(InputWaybillBase):
    pass


class InputWaybillUpdate(InputWaybillBase):
    status: Status


class InputWaybill(InputWaybillBase):
    id: int
    status: Status

    class Config:
        orm_mode = True
