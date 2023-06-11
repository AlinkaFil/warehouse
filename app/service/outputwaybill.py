from app.repository.outputwaybill import save, db_get_outputwaybill, db_get_outputwaybill_by_id, \
    db_put_change_outputwaybill, db_delete_outputwaybill
from app.base.outputwaybillbase import OutputWaybillBase, Status


def srv_create_outputwaybill(number):
    outputwaybill = OutputWaybillBase(number, Status.CREATED)
    return save(outputwaybill)


def srv_get_outputwaybill():
    return db_get_outputwaybill()


def srv_get_outputwaybill_by_id(ow_id):
    return db_get_outputwaybill_by_id(ow_id)


def srv_put_change_outputwaybill(ow_id, number, status):
    return db_put_change_outputwaybill(ow_id, number, status)


def srv_delete_outputwaybill(ow_id):
    return db_delete_outputwaybill(ow_id)
