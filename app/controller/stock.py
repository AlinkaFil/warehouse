from fastapi import FastAPI, Body
from app.service.stock import srv_create_stock, srv_get_stock, srv_get_stock_by_id, srv_put_change_stock, \
    srv_delete_stock
from app.scheme.stock import StockCreate, Stock, StockUpdate

app = FastAPI()


@app.post('/stock', response_model=Stock)
def create_stock(stock: StockCreate):
    return srv_create_stock(stock.vc_id, stock.qty)


@app.get("/stock", response_model=list[Stock])
def get_stock():
    return srv_get_stock()


@app.get("/stock/{id}", response_model=Stock)
def get_stock_by_id(id: int):
    return srv_get_stock_by_id(id)


@app.put("/stock/{id}", response_model=Stock)
def put_change_stock(id: int, stock: StockUpdate):
    return srv_put_change_stock(id, stock.qty)


@app.delete("/stock")
def delete_stock(id: int):
    return srv_delete_stock(id)
