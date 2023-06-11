from fastapi import HTTPException, APIRouter
from app.service.vendorcode import srv_create_vendor_code, srv_get_vendor_codes, srv_get_vendor_code_by_id, \
    srv_get_vendor_code_by_vendorCode, srv_put_change_vendor_code, srv_delete_vendor_code
from app.scheme.vendorCode import VendorCode, VendorCodeCreate, VendorCodeUpdate
from app.errors import VendorCodeError, VendorCodeIdError

router = APIRouter()


@router.post("/", response_model=VendorCode)
def create_vendor_code(vendor_code: VendorCodeCreate):
    try:
        return srv_create_vendor_code(vendor_code.vendor_сode, vendor_code.description)
    except VendorCodeError:
        raise HTTPException(status_code=403, detail='артикул уже существует')


@router.get("/", response_model=list[VendorCode])
def get_vendor_codes():
    return srv_get_vendor_codes()


@router.get("/{id}", response_model=VendorCode)
def get_vendor_code_by_id(id: int):
    try:
        return srv_get_vendor_code_by_id(id)
    except VendorCodeIdError:
        raise HTTPException(status_code=403, detail='id не найден')


@router.get("/", response_model=VendorCode)
def get_vendor_code_by_vendorCode(vendor_code: str):
    try:
        return srv_get_vendor_code_by_vendorCode(vendor_code)
    except VendorCodeError:
        raise HTTPException(status_code=403, detail='артикул не найден')


@router.put("/{id}", response_model=VendorCode)
def put_change_vendor_code(id: int, vendor_code: VendorCodeUpdate):
    try:
        return srv_put_change_vendor_code(id, vendor_code.description)
    except VendorCodeIdError:
        raise HTTPException(status_code=403, detail='id не найден')


@router.delete("/")
def delete_vendor_code(id: int):
    try:
        return srv_delete_vendor_code(id)
    except VendorCodeIdError:
        raise HTTPException(status_code=403, detail='id не найден')
