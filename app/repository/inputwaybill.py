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


def db_get_inputwaybill():
    session = new_session()
    inputwaybill = session.query(InputWaybillBase).all()
    return inputwaybill


def db_get_inputwaybill_by_id(iw_id):
    session = new_session()
    inputwaybill = session.query(InputWaybillBase).filter_by(id=iw_id).first()
    return inputwaybill


def db_put_change_inputwaybill(iw_id, number,status):
    session = new_session()
    inputwaybill1 = session.query(InputWaybillBase).filter_by(id=iw_id).first()
    inputwaybill1.number = number
    inputwaybill1.status=status
    session.commit()
    session.refresh(inputwaybill1)
    return inputwaybill1


def db_delete_inputwaybill(iw_id):
    session = new_session()
    session.query(InputWaybillBase).filter_by(id=iw_id).delete()
    session.commit()
