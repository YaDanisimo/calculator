from tokenizer import tokenize
from rpn_builder import to_rpn
from evaluator import evaluate
from formatter import to_format
from errors import *


def split_into_words(text):
    return text.lower().replace("ё", "е").split()


def calc(text):
    words = split_into_words(text)
    tokens = tokenize(words)
    rpn_expression = to_rpn(tokens)
    result = evaluate(rpn_expression)
    return to_format(result)


def interactive():
    while True:
        try:
            text = input()
        except EOFError:
            break
        except KeyboardInterrupt:
            break

        if not text.strip():
            continue

        try:
            answer = calc(text)
        except CalculatorError as e:
            print(e.message)
            continue
        except Exception as e:
            print(f"непредвиденная ошибка: {e}")
            continue

        print(answer)

if __name__ == "__main__":
    interactive()