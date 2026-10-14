from errors import InvalidSequenceError, UnknownWordError
from tokens import *
import converter


UNARY_OPERAND_POSITION = (OPERATOR, FUNCTION, OPENED_PAREN, START)
AWAITING_OPERATOR_POSITION = (NUMBER, CONSTANT, CLOSED_PAREN)


def consume_number_phrase(words, start):
    idx = start
    int_part = 0
    while idx < len(words) and words[idx] in converter.string_to_number_dictionary:
        int_part += converter.string_to_number_dictionary[words[idx]]
        idx += 1




def is_unary_position(prev_type):
    return prev_type in UNARY_OPERAND_POSITION

def is_operand_end(prev_type):
    return prev_type in AWAITING_OPERATOR_POSITION

def handle_number(word, prev_type):
    if prev_type == NUMBER:
        return Number(converter.get_number(word)), ADD
    if is_unary_position(prev_type):
        return Number(converter.get_number(word)), PUSH

    raise InvalidSequenceError(f"{word}")

def handle_operator(word, prev_type):
    is_unary = is_unary_position(prev_type)
    operator_symbol, priority, left_association = converter.get_operator(word)
    if is_unary and operator_symbol != "-":
        raise InvalidSequenceError(f"{word}")

    if is_unary:
        priority = UNARY_PRIORITY

    return Operator(operator_symbol, priority, left_association, is_unary), PUSH

def handle_opened_paren(word, prev_type):
    if not is_unary_position(prev_type): # сделать по умолчанию умножение между разными скобками "(...)(...)"
        raise InvalidSequenceError(f"{word}") # сделать отдельную функцию, которая показывает прошлый элемент

    return OpenedParen(), PUSH

def handle_closed_paren(word, prev_type):
    if not is_operand_end(prev_type):  # сделать по умолчанию умножение между разными скобками "(...)(...)"
        raise InvalidSequenceError(f"{word}")  # сделать отдельную функцию, которая показывает прошлый элемент

    return ClosedParen(), PUSH


_HANDLERS = {
    NUMBER: handle_number,
    OPERATOR: handle_operator,
    OPENED_PAREN: handle_opened_paren,
    CLOSED_PAREN: handle_closed_paren
}


def dispatcher(word, word_type, prev_word_type):
    handler = _HANDLERS.get(word_type)

    if handler is None:
        raise InvalidSequenceError(f"{word}")

    return handler(word, prev_word_type)


def request_processing(request: int, obj, expression: list):
    if request == ADD:
        expression[-1].value += obj.value
    elif request == PUSH:
        expression.append(obj)

def tokenize(text) -> list:
    words = text.split() + ["END"]

    prev_word_type = START
    expression = []

    idx = 0
    while idx < len(words):
        if words[idx] in converter.string_to_number_dictionary:



        for length in range(MAX_PHRASE_LENGTH, 0, -1):
            word = " ".join(words[idx:idx + length])
            word_type = converter.get_type(word)
            if word_type is None:
                continue
            finished_object, request = dispatcher(word, word_type, prev_word_type)
            request_processing(request, finished_object, expression)
            left_idx += length - 1
            break

        if word_type is None:
            raise UnknownWordError(f"Неизвестное слово '{word}'")

        left_idx += 1
        prev_word_type = word_type

    if prev_word_type in (FUNCTION, OPERATOR, OPENED_PAREN):
        raise InvalidSequenceError("незавершённое выражение")
    return expression