from sqlalchemy.orm import sessionmaker
from app.base.db import new_connect
from app.base.inputposbase import InputPosBase


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


def db_get_input_pos():
    session = new_session()
    input_pos = session.query(InputPosBase).all()
    return input_pos


def db_get_input_pos_by_id(ip_id):
    session = new_session()
    input_pos = session.query(InputPosBase).filter_by(id=ip_id).first()
    return input_pos


def db_put_change_input_pos(ip_id, qty):
    session = new_session()
    input_pos1 = session.query(InputPosBase).filter_by(id=ip_id).first()
    input_pos1.qty = qty
    session.commit()
    session.refresh(input_pos1)
    return input_pos1


def db_delete_input_pos(ip_id):
    session = new_session()
    session.query(InputPosBase).filter_by(id=ip_id).delete()
    session.commit()

