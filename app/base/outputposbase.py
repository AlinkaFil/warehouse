from sqlalchemy import Column, Integer, ForeignKey
from app.base.outputwaybillbase import OutputWaybillBase
from app.base.vendorcodebase import VendorCodeBase
from sqlalchemy.orm import declarative_base

Base_op = declarative_base()


class OutputPosBase(Base_op):
    __tablename__ = "OutputPos"
    id = Column(Integer, primary_key=True)
    ow_id = Column(Integer, ForeignKey(OutputWaybillBase.id))
    vc_id = Column(Integer, ForeignKey(VendorCodeBase.id))
    qty = Column(Integer)

    def __init__(self, ow_id, vc_id, qty):
        self.ow_id = ow_id
        self.vc_id = vc_id
        self.qty = qty

    def __repr__(self):
        return "<User('%s','%s','%s','%s')>" % (self.id, self.ow_id, self.vc_id, self.qty)