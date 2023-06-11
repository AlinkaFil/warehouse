from app.repository.outputwaybill import save, db_get_output_waybill, db_get_output_waybill_by_id, \
    db_put_change_output_waybill, db_delete_output_waybill
from app.base.outputwaybillbase import OutputWaybillBase, Status


def srv_create_output_waybill(number):
    output_waybill = OutputWaybillBase(number, Status.CREATED)
    return save(output_waybill)


def srv_get_output_waybill():
    return db_get_output_waybill()


def srv_get_output_waybill_by_id(ow_id):
    return db_get_output_waybill_by_id(ow_id)


def srv_put_change_output_waybill(ow_id, number, status):
    return db_put_change_output_waybill(ow_id, number, status)


def srv_delete_output_waybill(ow_id):
    return db_delete_output_waybill(ow_id)
