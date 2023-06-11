from pydantic import BaseModel


class OutputPosBase(BaseModel):
    ow_id: int
    vc_id: int
    qty: int


class OutputPosCreate(OutputPosBase):
    pass


class OutputPos(OutputPosBase):
    id: int

    class Config:
        orm_mode = True
