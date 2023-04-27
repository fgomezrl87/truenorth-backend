from fastapi import APIRouter, HTTPException
from app.models.operator_model import Operator, RandomString, Result, ResultString
from constants import COSTS
from app.services.utils import Utils
from app.services.calculator import Calculator

router = APIRouter()
utils = Utils()
calc = Calculator()


@router.post("/operator", response_model=Result)
async def operator_endpoint(operator: Operator):
    if operator.operation_type not in COSTS:
        raise HTTPException(status_code=400, detail="Invalid operation type")

    operation_cost = COSTS[operator.operation_type]

    if not utils.check_user_balance(operator.user_balance, operation_cost):
        raise HTTPException(status_code=403, detail="Insufficient balance")

    # We can now use the calculator after validations
    a = operator.a
    b = operator.b

    if operator.operation_type == "addition":
        result = calc.add(a, b)
    elif operator.operation_type == "subtraction":
        result = calc.subtract(a, b)
    elif operator.operation_type == "multiplication":
        result = calc.multiply(a, b)
    elif operator.operation_type == "division":
        result = calc.divide(a, b)
    elif operator.operation_type == "square_root":
        result = calc.square_root(a)
    elif operator.operation_type == "random_string":
        result = calc.random_string()
    else:
        raise HTTPException(status_code=400, detail="Invalid operation type")

    new_balance = operator.user_balance - operation_cost

    result: Result = Result(
        result=result,
        new_balance=new_balance
    )

    return result


@router.post("/random_string/{length}", response_model=ResultString)
async def generate_random_string(length: int, random_string: RandomString):
    operation_type = "random_string"
    operation_cost = COSTS[operation_type]

    if not utils.check_user_balance(random_string.user_balance, operation_cost):
        raise HTTPException(status_code=403, detail="Insufficient balance")

    random_str = calc.generate_random_string(length)

    new_balance = random_string.user_balance - operation_cost

    result: ResultString = ResultString(
        result=random_str,
        new_balance=new_balance
    )

    return result
