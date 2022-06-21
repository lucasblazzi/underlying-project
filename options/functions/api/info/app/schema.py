from pydantic import BaseModel, Field
#migrate to schema.py
class OptionIput(BaseModel):
    name: str = Field(None, min_length=5, max_length=8)
    id: str = Field(None, min_length=32, max_length=32)