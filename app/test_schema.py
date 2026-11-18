
from pydantic import BaseModel

class Invoice(BaseModel):
    invoice_number: str
    vendor: str
    total: float

invoice = Invoice(
    invoice_number="INV-001",
    vendor="ABC Technologies",
    total=500.0
)

print(invoice)
print(invoice.total)
print(invoice.model_dump())
