from fastapi import APIRouter
from app.service.outputpos import srv_create_output_pos, srv_get_output_pos, srv_put_change_output_pos, \
    srv_delete_output_pos, srv_get_output_pos_by_id
from app.scheme.outputpos import OutputPos, OutputPosCreate

router = APIRouter()


@router.post('/', response_model=OutputPos)
def create_output_pos(output_pos: OutputPosCreate):
    return srv_create_output_pos(output_pos.ow_id, output_pos.vc_id, output_pos.qty)


@router.get("/", response_model=list[OutputPos])
def get_output_pos():
    return srv_get_output_pos()


@router.get("/{id}", response_model=OutputPos)
def get_output_pos_by_id(id: int):
    return srv_get_output_pos_by_id(id)


@router.put("/{id}", response_model=OutputPos)
def put_change_output_pos(id: int, output_pos: OutputPosCreate):
    return srv_put_change_output_pos(id, output_pos.qty)


@router.delete("/{id}")
def delete_output_pos(id: int):
    return srv_delete_output_pos(id)
