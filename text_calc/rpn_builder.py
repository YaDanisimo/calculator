from tokens import *
from errors import (
    EmptyExpressionError,
    BracketBalanceError,
    InvalidSequenceError,
)


def _apply_operand_effect(count, op):
    if op.is_unary:
        if count < 1:
            raise InvalidSequenceError("не хватает операнда для оператора")
        return count
    if count < 2:
        raise InvalidSequenceError("не хватает операндов для оператора")
    return count - 1


def to_rpn(tokens):
    if not tokens:
        raise EmptyExpressionError()

    stack = []
    output = []
    count = 0

    for token in tokens:
        if isinstance(token, Number):
            output.append(token)
            count += 1
        elif isinstance(token, (Function, OpenBracket)):
            stack.append(token)
        elif isinstance(token, CloseBracket):
            while stack and not isinstance(stack[-1], OpenBracket):
                op = stack.pop()
                output.append(op)
                count = _apply_operand_effect(count, op)
            if not stack:
                raise BracketBalanceError("лишняя закрывающая скобка")
            stack.pop()
        else:  # Operator
            while stack:
                last = stack[-1]
                if not isinstance(last, Operator):
                    break
                should_pop = (
                    last.priority > token.priority
                    or (
                        last.priority == token.priority
                        and (last.association == LEFT or isinstance(last, UnarySub))
                    )
                )
                if should_pop:
                    op = stack.pop()
                    output.append(op)
                    count = _apply_operand_effect(count, op)
                else:
                    break
            stack.append(token)

    while stack:
        top = stack.pop()
        if isinstance(top, OpenBracket):
            raise BracketBalanceError("не закрыты скобки")
        output.append(top)
        count = _apply_operand_effect(count, top)

    return output