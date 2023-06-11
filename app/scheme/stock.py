from pydantic import BaseModel


class StockBase(BaseModel):
    qty: int


class StockCreate(StockBase):
    vc_id: int


class StockUpdate(StockBase):
    pass


class Stock(StockBase):
    id: int
    vc_id: int

    class Config:
        orm_mode = True
