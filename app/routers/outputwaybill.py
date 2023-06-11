from fastapi import APIRouter
from app.scheme.outputwaybill import OutputWaybill, OutputWaybillUpdate, OutputWaybillCreate
from app.service.outputwaybill import srv_create_output_waybill, srv_get_output_waybill_by_id, \
    srv_put_change_output_waybill, srv_delete_output_waybill, srv_get_output_waybill

router = APIRouter()


@router.post('/', response_model=OutputWaybill)
def create_output_waybill(output_waybill: OutputWaybillCreate):
    return srv_create_output_waybill(output_waybill.number)


@router.get("/", response_model=list[OutputWaybill])
def get_output_waybill():
    return srv_get_output_waybill()


@router.get("/{id}", response_model=OutputWaybill)
def get_output_waybill_by_id(id: int):
    return srv_get_output_waybill_by_id(id)


@router.put("/{id}", response_model=OutputWaybill)
def put_change_output_waybill(id: int, outputwaybill: OutputWaybillUpdate):
    return srv_put_change_output_waybill(id, outputwaybill.number, outputwaybill.status)


@router.delete("/{id}")
def delete_output_waybill(id: int):
    return srv_delete_output_waybill(id)
