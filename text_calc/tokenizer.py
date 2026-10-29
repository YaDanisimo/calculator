from converter import get_object_info
from tokens import *


create_operator = {
    PLUS: Add(),
    MINUS: Sub(is_unary=False),
    MUL: Mul(),
    DIV: Div(),
    POW: Pow(),
    SIN: Sin(),
    COS: Cos(),
    TAN: Tan()
}
def numerator_handler(value, prev_token):
    if isinstance(prev_token, CloseBracket):
        return None, ERROR

    if not isinstance(prev_token, Number):
        return Number(numerator=value), PUSH

    if prev_token.numerator




def denominator_handler(value, prev_token):
    return 2
def operator_handler(value, prev_token):
    if prev_token not in (OPEN_BRACKET, OPERATOR, None):
        return create_operator[value], PUSH

    if value == MINUS:
        new_operator = Sub(is_unary=True)
        return new_operator, PUSH

    return None, ERROR


create_token = {
    NUMERATOR: numerator_handler,
    DENOMINATOR: denominator_handler,
    OPERATOR: operator_handler
}

def command_apply(tokens, value, command):
    if command == PUSH:
        tokens.append(value)
        return
    if command == MERGE:
        if value


def tokenize(words: list):
    tokens = []

    len_words = len(words)
    left_idx = 0
    while left_idx < len_words:
        for shift in range(2, -1, -1):
            right_idx = min(left_idx + shift, len_words)
            potential_object = " ".join(words[left_idx:right_idx + 1])
            type_info, value = get_object_info(potential_object)

            if type_info is None: continue

            prev_token = tokens[-1] if tokens else None
            token = create_token[type_info](value, prev_token)
            tokens.append(token)
            break
        else: # неправильный ввод
            return None

        left_idx = right_idx + 1

    return tokens

words1 = ["два", "возвести", "в", "степень", "плюс", "синус", "от", "минус", "тридцать", "три"]
print(tokenize(words1))