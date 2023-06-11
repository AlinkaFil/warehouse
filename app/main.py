from fastapi import FastAPI, APIRouter
from app.routers import vendorcode, inputwaybill, inputpos, stock, outputwaybill, outputpos

app = FastAPI()
routes = APIRouter()

routes.include_router(vendorcode.router, prefix="/vendor-codes", tags=['Vendor code'])
routes.include_router(inputwaybill.router, prefix="/input-waybill", tags=['Input waybill'])
routes.include_router(inputpos.router, prefix="/input-pos", tags=['Input pos'])
routes.include_router(stock.router, prefix="/stock", tags=['Stock'])
routes.include_router(outputwaybill.router, prefix="/output-waybill", tags=['Output waybill'])
routes.include_router(outputpos.router, prefix="/output-pos", tags=['Output pos'])

app.include_router(routes)
