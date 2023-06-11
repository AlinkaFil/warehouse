from app.repository.inputwaybill import db_get_inputwaybill, db_get_inputwaybill_by_id, \
    db_put_change_inputwaybill, db_delete_inputwaybill, save
from app.base.inputwaybillbase import InputWaybillBase, Status


def srv_create_inputwaybill(number):
    inputwaybill = InputWaybillBase(number, Status.CREATED)
    return save(inputwaybill)


def srv_get_inputwaybill():
    return db_get_inputwaybill()


def srv_get_inputwaybill_by_id(iw_id):
    return db_get_inputwaybill_by_id(iw_id)


def srv_put_change_inputwaybill(iw_id, number,status):
    return db_put_change_inputwaybill(iw_id, number,status)


def srv_delete_inputwaybill(iw_id):
    return db_delete_inputwaybill(iw_id)
