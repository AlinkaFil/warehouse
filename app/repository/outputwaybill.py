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


def db_get_output_waybill():
    session = new_session()
    outputwaybill1 = session.query(OutputWaybillBase).all()
    return outputwaybill1


def db_get_output_waybill_by_id(ow_id):
    session = new_session()
    output_waybill = session.query(OutputWaybillBase).filter_by(id=ow_id).first()
    return output_waybill


def db_put_change_output_waybill(ow_id, number, status):
    session = new_session()
    output_waybill = session.query(OutputWaybillBase).filter_by(id=ow_id).first()
    output_waybill.number = number
    output_waybill.status = status
    session.commit()
    session.refresh(output_waybill)
    return output_waybill


def db_delete_output_waybill(ow_id):
    session = new_session()
    session.query(OutputWaybillBase).filter_by(id=ow_id).delete()
    session.commit()
