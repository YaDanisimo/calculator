class CalcError(Exception):
    pass

class TokenizerError(CalcError):
    pass

class ParserError(CalcError):
    pass

class EvaluatorError(CalcError):
    pass

class UnknownWordError(TokenizerError):
    def __init__(self, word):
        self.word = word
        super().__init__(f"Неизвестное слово: {word}")

class InvalidSequenceError(TokenizerError):
    def __init__(self, message):
        self.message = message
        super().__init__(f"Неправильная последовательность: {message}")

class InvalidNumberError(TokenizerError):
    def __init__(self, number):
        self.number = number
        super().__init__(f"Некорректная запись числа: {number}")

class MismatchedParenError(ParserError):
    def __init__(self, mismatch_open_paren: bool):
        self.paren_type = mismatch_open_paren
        error = "Незакрытая скобка" if mismatch_open_paren \
            else "Лишняя закрывающая скобка"
        super().__init__(error)

class DivisionByZeroError(EvaluatorError):
    def __init__(self):
        super().__init__("Деление на ноль")

class UnknownUnaryError(EvaluatorError):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class UnknownOperatorError(TokenizerError):
    def __init__(self, message):
        self.message = message
        super().__init__(message)