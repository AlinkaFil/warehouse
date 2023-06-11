from fastapi import FastAPI
from app.service.inputpos import srv_create_input_pos, srv_get_input_pos, srv_get_input_pos_by_id, \
    srv_put_change_input_pos, srv_delete_input_pos
from app.scheme.inputpos import InputPos, InputPosCreate

app = FastAPI()


@app.post('/input-pos', response_model=InputPos)
def create_input_pos(input_pos: InputPosCreate):
    return srv_create_input_pos(input_pos.iw_id, input_pos.vc_id, input_pos.qty)


@app.get("/input-pos", response_model=list[InputPos])
def get_input_pos():
    return srv_get_input_pos()


@app.get("/input-pos/{id}", response_model=InputPos)
def get_input_pos_by_id(id: int):
    return srv_get_input_pos_by_id(id)


@app.put("/input-pos/{id}", response_model=InputPos)
def put_change_input_pos(id: int, input_pos: InputPosCreate):
    return srv_put_change_input_pos(id, input_pos.qty)


@app.delete("/inpus-pos/{id}")
def delete_input_pos(id: int):
    return srv_delete_input_pos(id)
