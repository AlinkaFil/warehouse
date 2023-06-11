from app.repository.vendorcode import save, db_get_vendor_code_by_id, db_get_vendor_codes, \
    db_get_vendor_code_by_vendorCode, db_put_change_vendor_code, db_delete_vendor_code
from app.base.vendorcodebase import VendorCodeBase
from app.errors import VendorCodeError, VendorCodeIdError


def srv_create_vendor_code(vendor_сode, description):
    vendor_code = db_get_vendor_code_by_vendorCode(vendor_сode)
    if vendor_code is None:
        vendor_code1 = VendorCodeBase(vendor_сode, description)
        return save(vendor_code1)
    else:
        raise VendorCodeError


def srv_get_vendor_codes():
    return db_get_vendor_codes()


def srv_get_vendor_code_by_id(vc_id):
    vc_id1 = db_get_vendor_code_by_id(vc_id)
    if vc_id1 is  not None:
        return db_get_vendor_code_by_id(vc_id)
    else:
        raise VendorCodeIdError


def srv_get_vendor_code_by_vendorCode(vendor_сode):
    vendor_code = db_get_vendor_code_by_vendorCode(vendor_сode)
    if vendor_code is not None:
        return db_get_vendor_code_by_vendorCode(vendor_сode)
    else:
        raise VendorCodeError


def srv_put_change_vendor_code(vc_id, description):
    vc_id1 = db_get_vendor_code_by_id(vc_id)
    if vc_id1 is not None:
        return db_put_change_vendor_code(vc_id, description)
    else:
        raise VendorCodeIdError


def srv_delete_vendor_code(vc_id):
    vc_id1 = db_get_vendor_code_by_id(vc_id)
    if vc_id1 is not None:
        return db_delete_vendor_code(vc_id)
    else:
        raise VendorCodeIdError
