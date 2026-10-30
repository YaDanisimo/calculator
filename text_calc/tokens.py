# для конвертера
NUMERATOR = 0
DENOMINATOR = 1
OPERATOR = 2
OPEN_BRACKET = 3
CLOSE_BRACKET = 4


#команды для tokenizer
PUSH, MERGE_NUM, MERGE_DEN, ERROR = 0, 1, 2, 3

#списки десятков и единиц
TENS = range(10, 100, 10)
ONES = range(0, 10)

# общее
ADD, SUB, MUL, DIV, POW, SIN, COS, TAN, OPEN, CLOSE = range(0, 10)

class Number:
    def __init__(self, numerator=None, denominator=None):
        self.numerator = numerator
        self.denominator = denominator

LEFT, RIGHT = 0, 1 # ассоциативность
class Operator:
    def __init__(self, priority: int, association: int, is_unary: bool):
        self.priority = priority
        self.association = association
        self.is_unary = is_unary

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

class Pow(Operator):
    def __init__(self):
        super().__init__(3, RIGHT, False)


class Function(Operator):
    def __init__(self):
        super().__init__(3, RIGHT, True)

class Sin(Function):
    pass

class Cos(Function):
    pass

class Tan(Function):
    pass


class OpenBracket:
    pass

class CloseBracket:
    pass