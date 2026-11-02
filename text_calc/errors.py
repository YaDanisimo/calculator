class CalculatorError(Exception):
    default_message = "ошибка калькулятора"

    def __init__(self, message=None):
        self.message = message if message is not None else self.default_message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class TokenizeError(CalculatorError):
    default_message = "ошибка разбора выражения"

    def __init__(self, message=None, position=None):
        super().__init__(message)
        self.position = position


class EmptyExpressionError(TokenizeError):
    default_message = "пустое выражение"


class UnknownWordError(TokenizeError):
    def __init__(self, word, position=None):
        super().__init__(f"неизвестное слово: '{word}'", position)
        self.word = word


class InvalidNumberError(TokenizeError):
    default_message = "неверная запись числа"

    def __init__(self, phrase=None, position=None):
        self.phrase = phrase
        if phrase is not None:
            super().__init__(f"неверная запись числа: '{phrase}'", position)
        else:
            super().__init__(None, position)


class InvalidSequenceError(TokenizeError):
    default_message = "неверная последовательность чисел и операций"

    def __init__(self, phrase=None, position=None):
        self.phrase = phrase
        if phrase is not None:
            super().__init__(f"неверная последовательность: '{phrase}'", position)
        else:
            super().__init__(None, position)


class DecimalSeparatorError(TokenizeError):
    default_message = "ошибка в записи десятичной дроби"


class BracketBalanceError(TokenizeError):
    default_message = "неверный баланс скобок"


class BracketNestingError(TokenizeError):
    default_message = "неверная вложенность скобок"


class EvalError(CalculatorError):
    default_message = "ошибка вычисления"


class DivisionByZeroError(EvalError):
    default_message = "деление на ноль"


class ModuloByZeroError(EvalError):
    default_message = "остаток от деления на ноль"


class NegativeBaseFractionalExponentError(EvalError):
    default_message = "отрицательное основание в дробной степени"


class ZeroToNegativePowerError(EvalError):
    default_message = "ноль в отрицательной степени"


class TrigonometricUndefinedError(EvalError):
    default_message = "тригонометрическая функция не определена в этой точке"


class StackError(EvalError):
    default_message = "внутренняя ошибка вычисления: некорректное состояние стека"