from app.repository.inputwaybill import db_get_input_waybill, db_get_input_waybill_by_id, \
    db_put_change_input_waybill, save, db_delete_input_waybill
from app.base.inputwaybillbase import InputWaybillBase, Status


def srv_create_input_waybill(number):
    input_waybill = InputWaybillBase(number, Status.CREATED)
    return save(input_waybill)


def srv_get_input_waybill():
    return db_get_input_waybill()


def srv_get_input_waybill_by_id(iw_id):
    return db_get_input_waybill_by_id(iw_id)


def srv_put_change_input_waybill(iw_id, number, status):
    return db_put_change_input_waybill(iw_id, number, status)


def srv_delete_input_waybill(iw_id):
    return db_delete_input_waybill(iw_id)
