from converter import get_object_info
from tokens import *
from errors import (
    UnknownWordError,
    InvalidNumberError,
    InvalidSequenceError,
    DecimalSeparatorError,
    BracketNestingError,
)


create_operator = {
    ADD: Add(),
    SUB: Sub(),
    MUL: Mul(),
    DIV: Div(),
    MOD: Mod(),
    POW: Pow(),
    SIN: Sin(),
    COS: Cos(),
    TAN: Tan(),
    SIN_LOW: SinCapture(),
    COS_LOW: CosCapture(),
    TAN_LOW: TanCapture(),
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
    if value in (SIN, COS, TAN):
        if isinstance(prev_token, (Number, CloseBracket)):
            return None, ERROR
        return create_operator[value], PUSH

    if value in (SIN_LOW, COS_LOW, TAN_LOW):
        if isinstance(prev_token, (Number, CloseBracket, UnarySub)):
            return None, ERROR
        return create_operator[value], PUSH

    if isinstance(prev_token, (Number, CloseBracket)):
        return create_operator[value], PUSH

    if value == SUB:
        return UnarySub(), PUSH

    return None, ERROR


def bracket_handler(value, prev_token):
    if value == OPEN:
        if not isinstance(prev_token, (Number, CloseBracket)):
            return OpenBracket(), PUSH
    if value == CLOSE:
        if isinstance(prev_token, (Number, CloseBracket)):
            return CloseBracket(), PUSH
    return None, ERROR


def constant_handler(value, prev_token):
    if isinstance(prev_token, Number):
        num = prev_token.numerator * value.numerator
        den = (prev_token.denominator or 1) * value.denominator
        return Number(num, den), REPLACE
    if prev_token is None or isinstance(prev_token, (OpenBracket, Operator)):
        return Number(value.numerator, value.denominator), PUSH
    return None, ERROR


def decimal_sep_handler(value, prev_token):
    if isinstance(prev_token, Number) and prev_token.denominator in (None, 1):
        return DecimalSep(), PUSH
    return None, ERROR


create_token = {
    NUMERATOR: numerator_handler,
    DENOMINATOR: denominator_handler,
    OPERATOR: operator_handler,
    OPEN_BRACKET: bracket_handler,
    CLOSE_BRACKET: bracket_handler,
    CONSTANT: constant_handler,
    DECIMAL_SEP: decimal_sep_handler,
}


def command_apply(tokens, value, command):
    if command == PUSH:
        tokens.append(value)
    elif command == MERGE_NUM:
        tokens[-1].numerator += value
    elif command == MERGE_DEN:
        tokens[-1].denominator = value
    elif command == REPLACE:
        tokens[-1] = value


def set_denominator(number):
    if number.denominator is None:
        number.denominator = 1


def make_error(type_info, phrase, position):
    if type_info in (NUMERATOR, DENOMINATOR):
        return InvalidNumberError(phrase, position)
    if type_info == OPERATOR:
        return InvalidSequenceError(phrase, position)
    if type_info in (OPEN_BRACKET, CLOSE_BRACKET):
        return BracketNestingError(f"недопустимая скобка: '{phrase}'", position)
    if type_info == CONSTANT:
        return InvalidSequenceError(phrase, position)
    return DecimalSeparatorError(f"недопустимое 'и': '{phrase}'", position)


def merge_decimals(tokens):
    result = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if isinstance(token, DecimalSep):
            if i == 0 or i == len(tokens) - 1:
                raise DecimalSeparatorError(
                    "разделитель целой и дробной части в начале или конце выражения", i)
            int_part = tokens[i - 1]
            frac_part = tokens[i + 1]
            if not isinstance(int_part, Number) or not isinstance(frac_part, Number):
                raise DecimalSeparatorError(
                    "разделитель целой и дробной части должен стоять между числами", i)
            if int_part.denominator not in (None, 1):
                raise DecimalSeparatorError(
                    "целая часть десятичной дроби не может быть дробной", i)
            if frac_part.denominator is None:
                raise DecimalSeparatorError(
                    "после разделителя должна идти дробная часть", i)
            int_num = int_part.numerator
            int_den = int_part.denominator or 1
            frac_num = frac_part.numerator
            frac_den = frac_part.denominator
            merged_num = int_num * frac_den + frac_num * int_den
            merged_den = int_den * frac_den
            result.pop()
            result.append(Number(merged_num, merged_den))
            i += 2
        else:
            result.append(token)
            i += 1
    return result


def tokenize(words):
    if not words:
        return []

    tokens = []
    len_words = len(words)
    left_idx = 0

    while left_idx < len_words:
        match_found = False

        for shift in range(2, -1, -1):
            right_idx = min(left_idx + shift, len_words - 1)
            potential_object = " ".join(words[left_idx:right_idx + 1])

            type_info, value = get_object_info(potential_object)
            if type_info is None:
                continue

            prev_token = tokens[-1] if tokens else None
            value, command = create_token[type_info](value, prev_token)

            if command == ERROR:
                raise make_error(type_info, potential_object, left_idx)

            command_apply(tokens, value, command)
            left_idx = right_idx + 1
            match_found = True
            break

        if not match_found:
            raise UnknownWordError(words[left_idx], left_idx)

    tokens = merge_decimals(tokens)

    for token in tokens:
        if isinstance(token, Number):
            set_denominator(token)

    return tokens