from app.repository.stock import save, db_get_stock, db_get_stock_by_id, db_put_change_stock, db_delete_stock
from app.base.stockbase import StockBase


def srv_create_stock(vc_id, qty):
    stock = StockBase(vc_id, qty)
    return save(stock)


def srv_get_stock():
    return db_get_stock()


def srv_get_stock_by_id(s_id):
    return db_get_stock_by_id(s_id)


def srv_put_change_stock(s_id, qty):
    return db_put_change_stock(s_id, qty)


def srv_delete_stock(s_id):
    return db_delete_stock(s_id)
