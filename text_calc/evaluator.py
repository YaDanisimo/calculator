import math
from fractions import Fraction

from tokens import *
from errors import (
    DivisionByZeroError,
    ModuloByZeroError,
    ZeroToNegativePowerError,
    NegativeBaseFractionalExponentError,
    TrigonometricUndefinedError,
    StackError,
    EvalError,
)


def float_to_number(value):
    if math.isnan(value) or math.isinf(value):
        raise EvalError("результат не определён")
    frac = Fraction(value).limit_denominator(1000000)
    return Number(frac.numerator, frac.denominator)


def _trig_to_number(value):
    frac = Fraction(value).limit_denominator(1000)
    return Number(frac.numerator, frac.denominator)


def _check_trig_arg(x):
    if math.isnan(x) or math.isinf(x):
        raise TrigonometricUndefinedError("аргумент тригонометрии не определён")


def unary_subtraction(number):
    return Number(-number.numerator, number.denominator)


def sinus(number):
    x = number.numerator / number.denominator
    _check_trig_arg(x)
    return _trig_to_number(math.sin(x))


def cosine(number):
    x = number.numerator / number.denominator
    _check_trig_arg(x)
    return _trig_to_number(math.cos(x))


def tangent(number):
    x = number.numerator / number.denominator
    _check_trig_arg(x)
    c = math.cos(x)
    if abs(c) < 1e-9:
        raise TrigonometricUndefinedError("тангенс не определён в этой точке")
    return _trig_to_number(math.sin(x) / c)


def addition(number1, number2):
    result = Fraction(number1.numerator, number1.denominator) + \
             Fraction(number2.numerator, number2.denominator)
    return Number(result.numerator, result.denominator)


def subtraction(number1, number2):
    result = Fraction(number1.numerator, number1.denominator) - \
             Fraction(number2.numerator, number2.denominator)
    return Number(result.numerator, result.denominator)


def multiplication(number1, number2):
    result = Fraction(number1.numerator, number1.denominator) * \
             Fraction(number2.numerator, number2.denominator)
    return Number(result.numerator, result.denominator)


def division(number1, number2):
    if number2.numerator == 0:
        raise DivisionByZeroError()
    result = Fraction(number1.numerator, number1.denominator) / \
             Fraction(number2.numerator, number2.denominator)
    return Number(result.numerator, result.denominator)


def modulo(number1, number2):
    if number2.numerator == 0:
        raise ModuloByZeroError()
    result = Fraction(number1.numerator, number1.denominator) % \
             Fraction(number2.numerator, number2.denominator)
    return Number(result.numerator, result.denominator)


def power(base, exp):
    num1, den1 = base.numerator, base.denominator
    num2, den2 = exp.numerator, exp.denominator
    exp_frac = Fraction(num2, den2)

    if exp_frac.denominator == 1:
        n = exp_frac.numerator
        if num1 == 0 and n < 0:
            raise ZeroToNegativePowerError()
        result = Fraction(num1, den1) ** n
        return Number(result.numerator, result.denominator)

    base_float = num1 / den1
    exp_float = float(exp_frac)
    if base_float < 0:
        raise NegativeBaseFractionalExponentError()
    if base_float == 0 and exp_float < 0:
        raise ZeroToNegativePowerError()
    result = base_float ** exp_float
    return float_to_number(result)


apply_operation = {
    UnarySub: unary_subtraction,
    Sin: sinus,
    Cos: cosine,
    Tan: tangent,
    SinCapture: sinus,
    CosCapture: cosine,
    TanCapture: tangent,
    Add: addition,
    Sub: subtraction,
    Mul: multiplication,
    Div: division,
    Mod: modulo,
    Pow: power,
}


def evaluate(rpn_expression):
    stack = []

    for obj in rpn_expression:
        if isinstance(obj, Number):
            stack.append(obj)
            continue

        handler = apply_operation[type(obj)]

        if obj.is_unary:
            if not stack:
                raise StackError("не хватает операнда для унарного оператора")
            number = stack.pop()
            stack.append(handler(number))
        else:
            if len(stack) < 2:
                raise StackError("не хватает операндов для бинарного оператора")
            right = stack.pop()
            left = stack.pop()
            stack.append(handler(left, right))

    if len(stack) != 1:
        raise StackError("в результате вычисления осталось не одно значение")

    return stack[0]