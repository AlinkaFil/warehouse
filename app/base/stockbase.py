from sqlalchemy import Column, Integer, ForeignKey
from app.base.vendorcodebase import VendorCodeBase as vc
from sqlalchemy.orm import declarative_base

Base_st = declarative_base()


class StockBase(Base_st):
    __tablename__ = "Stock"
    id = Column(Integer, primary_key=True)
    vc_id = Column(Integer, ForeignKey(vc.id))
    qty = Column(Integer)

    def __init__(self, vc_id, qty):
        self.vc_id = vc_id
        self.qty = qty

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.id, self.vc_id, self.qty)
