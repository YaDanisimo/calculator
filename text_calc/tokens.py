# для конвертера
NUMERATOR = 0
DENOMINATOR = 1
OPERATOR = 2
OPEN_BRACKET = 3
CLOSE_BRACKET = 4

#команды для tokenizer
PUSH, MERGE, ERROR = 0, 1, 2

# общее
PLUS, MINUS, MUL, DIV, POW, SIN, COS, TAN, OPEN, CLOSE = range(0, 10)

class Number:
    def __init__(self, rank, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.last_rank = rank

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
    def __init__(self, is_unary):
        priority, association = (3, RIGHT) if is_unary else (1, LEFT)
        super().__init__(priority, association, is_unary)

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