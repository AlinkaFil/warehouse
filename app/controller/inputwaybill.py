from fastapi import FastAPI
from app.service.inputwaybill import srv_create_inputwaybill, \
    srv_get_inputwaybill, srv_get_inputwaybill_by_id, \
    srv_put_change_inputwaybill, srv_delete_inputwaybill
from app.scheme.inputwaybill import InputWaybillCreate, InputWaybillBase, InputWaybillUpdate,InputWaybill

app = FastAPI()


@app.post('/inputwaybill', response_model=InputWaybill)
def create_inputwaybill(inputwaybill: InputWaybillCreate):
    return srv_create_inputwaybill(inputwaybill.number)




@app.get("/inputwaybill", response_model=list[InputWaybill])
def get_inputwaybill():
    return srv_get_inputwaybill()


@app.get("/inputwaybill/{id}", response_model=InputWaybill)
def get_inputwaybill_by_id(id: int):
    return srv_get_inputwaybill_by_id(id)


@app.put("/inputwaybill/{id}", response_model=InputWaybill)
def put_change_inputwaybill(id: int, inputwaybill: InputWaybillUpdate):
    return srv_put_change_inputwaybill(id, inputwaybill.number,inputwaybill.status)


@app.delete("/inputwaybill")
def delete_inputwaybill(id: int):
    return srv_delete_inputwaybill(id)
