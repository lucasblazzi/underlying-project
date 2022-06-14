from enum import Enum
from typing import List
from pydantic import BaseModel


class TransactionEnum(str, Enum):
    long = "LONG"
    short = "SHORT"


class TypeEnum(str, Enum):
    call = "CALL"
    put = "PUT"


class Option(BaseModel):
    id: str
    name: str
    type: str
    exercise_price: float
    transaction_type: str
    close_price: float
    contracts: int


class Strategy(BaseModel):
    username: str
    strategy: List[Option]