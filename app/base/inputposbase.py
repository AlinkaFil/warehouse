from sqlalchemy import Column, Integer, ForeignKey
from app.base.inputwaybillbase import InputWaybillBase
from app.base.vendorcodebase import VendorCodeBase
from sqlalchemy.orm import declarative_base

Base_ip = declarative_base()


class InputPosBase(Base_ip):
    __tablename__ = "InputPos"
    id = Column(Integer, primary_key=True)
    iw_id = Column(Integer, ForeignKey(InputWaybillBase.id))
    vc_id = Column(Integer, ForeignKey(VendorCodeBase.id))
    qty = Column(Integer)

    def __init__(self, iw_id, vc_id, qty):
        self.iw_id = iw_id
        self.vc_id = vc_id
        self.qty = qty

    def __repr__(self):
        return "<User('%s','%s','%s','%s')>" % (self.id, self.iw_id, self.vc_id, self.qty)
