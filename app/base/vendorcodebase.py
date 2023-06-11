from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base_vс = declarative_base()


class VendorCodeBase(Base_vс):
    __tablename__ = "VendorCode"
    id = Column(Integer, primary_key=True)
    vendor_сode = Column(String, unique=True)
    description = Column(String)

    def __init__(self, vendor_сode, description):
        self.vendor_сode = vendor_сode
        self.description = description

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.id, self.vendor_сode, self.description)
