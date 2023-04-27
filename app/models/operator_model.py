from pydantic import BaseModel


class Operator(BaseModel):
    operation_type: str
    a: float
    b: float
    user_balance: int


class RandomString(BaseModel):
    user_balance: int


class Result(BaseModel):
    result: float
    new_balance: int


class ResultString(BaseModel):
    result: str
    new_balance: int
