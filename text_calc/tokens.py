from errors import *

NUMERATOR = 0
DENOMINATOR = 1
OPERATOR = 2
OPEN_BRACKET = 3
CLOSE_BRACKET = 4
CONSTANT = 5
DECIMAL_SEP = 6

PUSH, MERGE_NUM, MERGE_DEN, ERROR, REPLACE = 0, 1, 2, 3, 4

ADD, SUB, MUL, DIV, MOD, POW, SIN, COS, TAN, SIN_LOW, COS_LOW, TAN_LOW, OPEN, CLOSE = range(0, 14)

TENS = range(20, 100, 10)
ONES = range(1, 10)

LEFT, RIGHT = 0, 1


class Number:
    def __init__(self, numerator=None, denominator=None):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f"Number({self.numerator!r}, {self.denominator!r})"


class Operator:
    def __init__(self, priority, association, is_unary):
        self.priority = priority
        self.association = association
        self.is_unary = is_unary

    def __repr__(self):
        return f"{self.__class__.__name__}({self.priority}, {self.association}, {self.is_unary})"


class Add(Operator):
    def __init__(self):
        super().__init__(1, LEFT, False)


class Sub(Operator):
    def __init__(self):
        super().__init__(1, LEFT, False)


class UnarySub(Operator):
    def __init__(self):
        super().__init__(3, RIGHT, True)


class Mul(Operator):
    def __init__(self):
        super().__init__(2, LEFT, False)


class Div(Operator):
    def __init__(self):
        super().__init__(2, LEFT, False)


class Mod(Operator):
    def __init__(self):
        super().__init__(2, LEFT, False)


class Pow(Operator):
    def __init__(self):
        super().__init__(3, RIGHT, False)


class Function(Operator):
    def __init__(self, priority):
        super().__init__(priority, RIGHT, True)


class Sin(Function):
    def __init__(self):
        super().__init__(5)


class Cos(Function):
    def __init__(self):
        super().__init__(5)


class Tan(Function):
    def __init__(self):
        super().__init__(5)


class SinCapture(Function):
    def __init__(self):
        super().__init__(1)


class CosCapture(Function):
    def __init__(self):
        super().__init__(1)


class TanCapture(Function):
    def __init__(self):
        super().__init__(1)


class OpenBracket:
    def __repr__(self):
        return "OpenBracket()"


class CloseBracket:
    def __repr__(self):
        return "CloseBracket()"


class DecimalSep:
    def __repr__(self):
        return "DecimalSep()"