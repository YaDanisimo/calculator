from errors import DivisionByZeroError
from errors import UnknownOperatorError
from tokens import *

EMPTY = object()

def apply_unary(number, operator):
    if operator == "-":
        return -number

    raise UnknownOperatorError(f"унарный {operator}")


def apply(first_number, second_number, operator):
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        if second_number == 0:
            raise DivisionByZeroError()
        return first_number / second_number
    if operator == "**":
        return first_number ** second_number


def calculate(rpn_expression):
    stack = []
    for obj in rpn_expression:
        if isinstance(obj, Number):
            stack.append(obj.value)

        elif isinstance(obj, Operator):
            operator = obj.operator
            if obj.unary:
                number = stack.pop()
                new_number = apply_unary(number, operator)
            else:
                second_number = stack.pop()
                first_number = stack.pop()
                operator = obj.operator
                new_number = apply(first_number, second_number, operator)

            stack.append(new_number)

    return stack[0]
