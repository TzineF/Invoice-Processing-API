
import uuid

from fastapi import APIRouter, File, HTTPException, UploadFile

router = APIRouter()

ALLOWED_CONTENT_TYPES = {
    "application/pdf",
    "image/jpeg",
    "image/png",
}

MAX_UPLOAD_BYTES = 10 * 1024 * 1024


@router.post("/invoices", status_code=202)
async def upload_invoice(file: UploadFile = File(...)):

    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=415,
            detail="Only PDF, JPEG, and PNG files are supported"
        )

    data = await file.read(MAX_UPLOAD_BYTES + 1)

    if not data:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty"
        )

    if len(data) > MAX_UPLOAD_BYTES:
        raise HTTPException(
            status_code=413,
            detail="File exceeds maximum upload size"
        )

    invoice_id = uuid.uuid4()

    return {
        "id": str(invoice_id),
        "filename": file.filename,
        "status": "uploaded",
        "message": "Invoice accepted for processing"
    }
