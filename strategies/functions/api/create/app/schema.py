from uuid import uuid4
from typing import List
from pydantic import BaseModel, validator, Field, StrictStr


VALID_TYPES = ("CALL", "PUT")
VALID_TRANSACTIONS = ("LONG", "SHORT")


class Option(BaseModel):
    name: str = Field(None, min_length=3, max_length=40)
    type: str
    exercise_price: float = Field(gt=0)
    transaction_type: str
    close_price: float = Field(gt=0)
    contracts: int = Field(gt=0)

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


class Strategy(BaseModel):
    name: str = Field(None, min_length=3, max_length=40)
    username: str = Field(None, min_length=6, max_length=20)
    id = str(uuid4())
    shared = False
    strategy: List[Option] = Field(min_items=1)
