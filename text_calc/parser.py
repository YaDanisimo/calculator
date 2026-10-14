from errors import MismatchedParenError
from tokens import *


def must_emit_first(head_operator, new_operator):
    if head_operator.priority > new_operator.priority or \
        head_operator.priority == new_operator.priority and \
         new_operator.left_association:
        return True
    return False


def top_is_operator(operators_stack: list):
    if operators_stack and isinstance(operators_stack[-1], Operator):
        return True
    return False


def to_reverse_polish_notation(expression):
    rpn_expression = []
    operators_stack = []

    for obj in expression:
        if isinstance(obj, Number):
            rpn_expression.append(obj)

        elif isinstance(obj, Operator):
            if not obj.unary:
                while top_is_operator(operators_stack) and must_emit_first(operators_stack[-1], obj):
                    rpn_expression.append(operators_stack.pop())
            operators_stack.append(obj)

        elif isinstance(obj, OpenedParen):
            operators_stack.append(obj)
        elif isinstance(obj, ClosedParen):
            while top_is_operator(operators_stack):
                rpn_expression.append(operators_stack.pop())

            if not operators_stack:
                raise MismatchedParenError(True)

            operators_stack.pop()

    while operators_stack:
        obj = operators_stack.pop()
        if isinstance(obj, OpenedParen):
            raise MismatchedParenError(False)
        rpn_expression.append(obj)

    return rpn_expression