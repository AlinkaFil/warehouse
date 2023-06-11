from sqlalchemy.orm import sessionmaker
from app.base.db import new_connect
from app.base.stockbase import StockBase


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


def db_get_stock():
    session = new_session()
    stock = session.query(StockBase).all()
    return stock


def db_get_stock_by_id(s_id):
    session = new_session()
    stock = session.query(StockBase).filter_by(id=s_id).first()
    return stock


def db_put_change_stock(s_id, qty):
    session = new_session()
    qty1 = session.query(StockBase).filter_by(id=s_id).first()
    qty1.qty = qty
    session.commit()
    session.refresh(qty1)
    return qty1


def db_delete_stock(s_id):
    session = new_session()
    session.query(StockBase).filter_by(id=s_id).delete()
    session.commit()
