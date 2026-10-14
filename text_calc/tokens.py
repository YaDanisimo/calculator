START, END, NUMBER, OPERATOR, OPENED_PAREN, CLOSED_PAREN, FUNCTION, CONSTANT = range(-2, 6)

UNARY_PRIORITY = 3
ADD, MUT, PUSH = 0, 1, 2
MAX_PHRASE_LENGTH = 3

class Number:
    def __init__(self, value):
        self.value = value

class Operator:
    def __init__(self, operator: str, priority: int, left_association: bool, unary: bool):
        self.operator = operator
        self.priority = priority
        self.left_association = left_association
        self.unary = unary

class OpenedParen:
    pass

class ClosedParen:
    pass
