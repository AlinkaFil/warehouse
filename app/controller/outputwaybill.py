from fastapi import FastAPI
from app.scheme.outputwaybill import OutputWaybill,OutputWaybillUpdate,OutputWaybillCreate
from app.service.outputwaybill import srv_create_outputwaybill, srv_get_outputwaybill, srv_get_outputwaybill_by_id, \
    srv_put_change_outputwaybill, srv_delete_outputwaybill

app = FastAPI()


@app.post('/outputwaybill', response_model=OutputWaybill)
def create_outputwaybill(outputwaybill: OutputWaybillCreate):
    return srv_create_outputwaybill(outputwaybill.number)




@app.get("/outputwaybill", response_model=list[OutputWaybill])
def get_outputwaybill():
    return srv_get_outputwaybill()


@app.get("/outputwaybill/{id}", response_model=OutputWaybill)
def get_outputwaybill_by_id(id: int):
    return srv_get_outputwaybill_by_id(id)


@app.put("/outputwaybill/{id}", response_model=OutputWaybill)
def put_change_outputwaybill(id: int, outputwaybill: OutputWaybillUpdate):
    return srv_put_change_outputwaybill(id, outputwaybill.number,outputwaybill.status)


@app.delete("/outputwaybill")
def delete_outputwaybill(id: int):
    return srv_delete_outputwaybill(id)
