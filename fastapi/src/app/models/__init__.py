from pydantic import BaseModel, validator
from sqlmodel import SQLModel


class ValidatedSQLModel(SQLModel):
    @validator("*")
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v


class ValidatedBaseModel(BaseModel):
    @validator("*")
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v
