from fastapi import APIRouter
from app.service.stock import srv_create_stock, srv_get_stock, srv_get_stock_by_id, srv_put_change_stock, \
    srv_delete_stock
from app.scheme.stock import StockCreate, Stock, StockUpdate

router = APIRouter()


@router.post('/', response_model=Stock)
def create_stock(stock: StockCreate):
    return srv_create_stock(stock.vc_id, stock.qty)


@router.get("/", response_model=list[Stock])
def get_stock():
    return srv_get_stock()


@router.get("/{id}", response_model=Stock)
def get_stock_by_id(id: int):
    return srv_get_stock_by_id(id)


@router.put("/{id}", response_model=Stock)
def put_change_stock(id: int, stock: StockUpdate):
    return srv_put_change_stock(id, stock.qty)


@router.delete("/{id}")
def delete_stock(id: int):
    return srv_delete_stock(id)
