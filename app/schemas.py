
from datetime import date
from pydantic import BaseModel, Field
from pydantic import model_validator
from typing import Self


class LineItem(BaseModel):
    description: str
    quantity: float = Field(ge=0)
    unit_price: float = Field(ge=0)
    tax_amount: float = Field(default=0, ge=0)
    line_total: float = Field(ge=0)


class InvoiceData(BaseModel):
    vendor_name: str
    invoice_number: str
    invoice_date: date
    currency: str
    line_items: list[LineItem]
    subtotal: float = Field(ge=0)
    total_tax: float = Field(default=0, ge=0)
    total_amount: float = Field(ge=0)



class ExtractionResult(BaseModel):
    is_invoice: bool
    invoice: InvoiceData | None
    confidence: float = Field(ge=0, le=1)
    warnings: list[str]

    @model_validator(mode="after")
    def invoice_must_match_flag(self) -> Self:
        if self.is_invoice and self.invoice is None:
            raise ValueError(
                "invoice is required when is_invoice is true"
            )
        return self