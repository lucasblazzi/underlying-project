from enum import Enum
from typing import List
from pydantic import BaseModel, validator


VALID_TYPES = ("CALL", "PUT")
VALID_TRANSACTIONS = ("LONG", "SHORT")


class Option(BaseModel):
    name: str
    type: str
    exercise_price: float
    transaction_type: str
    close_price: float
    contracts: int

    @validator("type")
    def validate_type(cls, v):
        if v.upper() not in VALID_TYPES:
            raise TypeError
        return v.upper()

    @validator("transaction_type")
    def validate_transaction(cls, v):
        if v.upper() not in VALID_TRANSACTIONS:
            raise TypeError
        return v.upper()


class Share(BaseModel):
    id: str
    shared: bool


class Delete(BaseModel):
    id: str
    deleted: bool