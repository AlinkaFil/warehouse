from fastapi import FastAPI, HTTPException
from app.service.vendorcode import srv_create_vendor_code, srv_get_vendor_codes, srv_get_vendor_code_by_id, \
    srv_get_vendor_code_by_vendorCode, srv_put_change_vendor_code, srv_delete_vendor_code
from app.scheme.vendorCode import VendorCode, VendorCodeCreate, VendorCodeUpdate
from app.errors import VendorCodeError, VendorCodeIdError

app = FastAPI()


@app.post("/vendor-codes", response_model=VendorCode)
def create_vendor_code(vendor_сode: VendorCodeCreate):
    try:
        return srv_create_vendor_code(vendor_сode.vendor_сode, vendor_сode.description)
    except VendorCodeError:
        raise HTTPException(status_code=403, detail='артикул уже существует')


@app.get("/vendor-codes", response_model=list[VendorCode])
def get_vendor_codes():
    return srv_get_vendor_codes()


@app.get("/vendor-Codes/{vc_id}", response_model=VendorCode)
def get_vendor_code_by_id(vc_id: int):
    try:
        return srv_get_vendor_code_by_id(vc_id)
    except VendorCodeIdError:
        raise HTTPException(status_code=403, detail='id не найден')


@app.get("/vendor-Codes", response_model=VendorCode)
def get_vendor_code_by_vendorCode(vendor_сode: str):
    try:
        return srv_get_vendor_code_by_vendorCode(vendor_сode)
    except VendorCodeError:
        raise HTTPException(status_code=403, detail='артикул не найден')


@app.put("/vendor-codes/{vc_id}", response_model=VendorCode)
def put_change_vendor_code(vc_id: int, vendor_сode: VendorCodeUpdate):
    try:
        return srv_put_change_vendor_code(vc_id, vendor_сode.description)
    except VendorCodeIdError:
        raise HTTPException(status_code=403, detail='id не найден')


@app.delete("/vendor-codes")
def delete_vendor_code(vs_id: int):
    try:
        return srv_delete_vendor_code(vs_id)
    except VendorCodeIdError:
        raise HTTPException(status_code=403, detail='id не найден')
