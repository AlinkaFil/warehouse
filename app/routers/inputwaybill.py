from fastapi import APIRouter
from app.service.inputwaybill import srv_create_input_waybill, srv_get_input_waybill, srv_get_input_waybill_by_id, \
    srv_put_change_input_waybill, srv_delete_input_waybill
from app.scheme.inputwaybill import InputWaybillCreate, InputWaybillUpdate, InputWaybill

router = APIRouter()


@router.post("/", response_model=InputWaybill)
def create_input_waybill(input_waybill: InputWaybillCreate):
    return srv_create_input_waybill(input_waybill.number)


@router.get("/", response_model=list[InputWaybill])
def get_input_waybill():
    return srv_get_input_waybill()


@router.get("/{id}", response_model=InputWaybill)
def get_input_waybill_by_id(id: int):
    return srv_get_input_waybill_by_id(id)


@router.put("/{id}", response_model=InputWaybill)
def put_change_input_waybill(id: int, input_waybill: InputWaybillUpdate):
    return srv_put_change_input_waybill(id, input_waybill.number, input_waybill.status)


@router.delete("/{id}")
def delete_input_waybill(id: int):
    return srv_delete_input_waybill(id)
