from converter import get_object_info
from tokens import *


create_operator = {
    ADD: Add(),
    SUB: Sub(),
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

    if prev_token.numerator is not None:
        can_merge = prev_token.numerator in TENS and value in ONES

        if can_merge and prev_token.denominator is None:
            return value, MERGE_NUM

    return None, ERROR

def denominator_handler(value, prev_token):
    if isinstance(prev_token, CloseBracket):
        return None, ERROR

    if not isinstance(prev_token, Number):
        return Number(numerator=1, denominator=value), PUSH

    if prev_token.denominator is None:
        return value, MERGE_DEN

    return None, ERROR

def operator_handler(value, prev_token):
    if isinstance(prev_token, (CloseBracket, Number)):
        return create_operator[value], PUSH

    if value == SUB:
        new_operator = UnarySub()
        return new_operator, PUSH

    if value in (SIN, COS, TAN):
        return create_operator[value], PUSH

    return None, ERROR


create_token = {
    NUMERATOR: numerator_handler,
    DENOMINATOR: denominator_handler,
    OPERATOR: operator_handler
}

def command_apply(tokens, value, command):
    if command == PUSH:
        tokens.append(value)
    elif command == MERGE_NUM:
        tokens[-1].numerator += value
    elif command == MERGE_DEN:
        tokens[-1].denominator =  value



def tokenize(words: list):
    tokens = []

    len_words = len(words)
    left_idx = 0
    while left_idx < len_words:
        print(tokens)
        match_found = False

        for shift in range(2, -1, -1):

            right_idx = min(left_idx + shift, len_words - 1)
            potential_object = " ".join(words[left_idx:right_idx + 1])
            print(potential_object)
            type_info, value = get_object_info(potential_object)
            print(type_info, value)
            if type_info is None: continue

            prev_token = tokens[-1] if tokens else None
            value, command = create_token[type_info](value, prev_token)
            print(tokens, value)
            if command == ERROR: return None

            command_apply(tokens, value, command)
            left_idx = right_idx + 1
            match_found = True
            break
        print(match_found)
        if not match_found:
            return None

    return tokens

words1 = ["один", "возвести", "в", "степень", "три", "плюс", "синус", "от", "минус", "тридцать", "три", "сотых"]
tokens1 = tokenize(words1)