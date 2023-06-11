from pydantic import BaseModel


class InputPosBase(BaseModel):
    iw_id: int
    vc_id: int
    qty: int


class InputPosCreate(InputPosBase):
    pass


class InputPos(InputPosBase):
    id: int

    class Config:
        orm_mode = True
