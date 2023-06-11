from app.repository.inputpos import save, db_get_input_pos, db_get_input_pos_by_id, db_put_change_input_pos, \
    db_delete_input_pos
from app.base.inputposbase import InputPosBase


def srv_create_input_pos(iw_id, vc_id, qty):
    input_pos = InputPosBase(iw_id, vc_id, qty)
    return save(input_pos)


def srv_get_input_pos():
    return db_get_input_pos()


def srv_get_input_pos_by_id(ip_id):
    return db_get_input_pos_by_id(ip_id)


def srv_put_change_input_pos(ip_id, qty):
    return db_put_change_input_pos(ip_id, qty)


def srv_delete_input_pos(ip_id):
    return db_delete_input_pos(ip_id)
