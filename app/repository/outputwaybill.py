from sqlalchemy.orm import sessionmaker
from app.base.db import new_connect
from app.base.outputwaybillbase import OutputWaybillBase


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


def db_get_outputwaybill():
    session = new_session()
    outputwaybill1 = session.query(OutputWaybillBase).all()
    return outputwaybill1


def db_get_outputwaybill_by_id(ow_id):
    session = new_session()
    outputwaybill = session.query(OutputWaybillBase).filter_by(id=ow_id).first()
    return outputwaybill


def db_put_change_outputwaybill(ow_id, number,status):
    session = new_session()
    outputwaybill1 = session.query(OutputWaybillBase).filter_by(id=ow_id).first()
    outputwaybill1.number = number
    outputwaybill1.status=status
    session.commit()
    session.refresh(outputwaybill1)
    return outputwaybill1


def db_delete_outputwaybill(ow_id):
    session = new_session()
    session.query(OutputWaybillBase).filter_by(id=ow_id).delete()
    session.commit()
