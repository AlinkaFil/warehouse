from pydantic import BaseModel

class VendorCodeBase(BaseModel):
    description: str | None = None


class VendorCodeCreate(VendorCodeBase):
    vendor_сode: str


class VendorCodeUpdate(VendorCodeBase):
    pass


class VendorCode(VendorCodeBase):
    vendor_сode: str
    id: int

    class Config:
        orm_mode = True
