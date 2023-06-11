from app.repository.outputpos import save, db_get_output_pos, db_get_output_pos_by_id, db_put_change_output_pos, \
    db_delete_output_pos
from app.base.outputposbase import OutputPosBase


def srv_create_output_pos(ow_id, vc_id, qty):
    output_pos = OutputPosBase(ow_id, vc_id, qty)
    return save(output_pos)


def srv_get_output_pos():
    return db_get_output_pos()



def srv_get_output_pos_by_id(op_id):
    return db_get_output_pos_by_id(op_id)


def srv_put_change_output_pos(op_id, qty):
    return db_put_change_output_pos(op_id, qty)


def srv_delete_output_pos(op_id):
    return db_delete_output_pos(op_id)
