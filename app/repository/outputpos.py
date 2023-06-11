from sqlalchemy.orm import sessionmaker
from app.base.db import new_connect
from app.base.outputposbase import OutputPosBase


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


def db_get_output_pos():
    session = new_session()
    output_pos = session.query(OutputPosBase).all()
    return output_pos


def db_get_output_pos_by_id(op_id):
    session = new_session()
    output_pos = session.query(OutputPosBase).filter_by(id=op_id).first()
    return output_pos


def db_put_change_output_pos(op_id, qty):
    session = new_session()
    output_pos1 = session.query(OutputPosBase).filter_by(id=op_id).first()
    output_pos1.qty = qty
    session.commit()
    session.refresh(output_pos1)
    return output_pos1


def db_delete_output_pos(op_id):
    session = new_session()
    session.query(OutputPosBase).filter_by(id=op_id).delete()
    session.commit()

