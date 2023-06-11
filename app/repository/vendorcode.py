from sqlalchemy.orm import sessionmaker
from app.base.vendorcodebase import VendorCodeBase
from app.base.db import new_connect


def new_session():
    engine = new_connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def save(x):
    session = new_session()
    session.add(x)
    session.commit()
    session.refresh(x)
    return x


def db_get_vendor_codes():
    session = new_session()
    vender_code = session.query(VendorCodeBase).all()
    return vender_code


def db_get_vendor_code_by_id(vc_id):
    session = new_session()
    vender_code = session.query(VendorCodeBase).filter_by(id=vc_id).first()
    return vender_code


def db_get_vendor_code_by_vendorCode(vendor_сode):
    session = new_session()
    vendor_сode = session.query(VendorCodeBase).filter_by(vendor_сode=vendor_сode).first()
    return vendor_сode


def db_put_change_vendor_code(vc_id, description):
    session = new_session()
    description1 = session.query(VendorCodeBase).filter_by(id=vc_id).first()
    description1.description = description
    session.commit()
    session.refresh(description1)
    return description1


def db_delete_vendor_code(vc_id):
    session = new_session()
    session.query(VendorCodeBase).filter_by(id=vc_id).delete()
    session.commit()
