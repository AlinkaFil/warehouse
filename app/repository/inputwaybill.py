from sqlalchemy.orm import sessionmaker
from app.base.db import new_connect
from app.base.inputwaybillbase import InputWaybillBase


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


def db_get_input_waybill():
    session = new_session()
    inputwaybill = session.query(InputWaybillBase).all()
    return inputwaybill


def db_get_input_waybill_by_id(iw_id):
    session = new_session()
    input_waybill = session.query(InputWaybillBase).filter_by(id=iw_id).first()
    return input_waybill


def db_put_change_input_waybill(iw_id, number, status):
    session = new_session()
    input_waybill = session.query(InputWaybillBase).filter_by(id=iw_id).first()
    input_waybill.number = number
    input_waybill.status = status
    session.commit()
    session.refresh(input_waybill)
    return input_waybill


def db_delete_input_waybill(iw_id):
    session = new_session()
    session.query(InputWaybillBase).filter_by(id=iw_id).delete()
    session.commit()
