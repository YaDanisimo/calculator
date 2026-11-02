import sys

from tokenizer import tokenize
from rpn_builder import to_rpn
from evaluator import evaluate
from formatter import format_number
from errors import *


def split_into_words(text):
    return text.lower().replace("ё", "е").split()


def calc(text):
    words = split_into_words(text)
    tokens = tokenize(words)
    rpn_expression = to_rpn(tokens)
    result = evaluate(rpn_expression)
    return format_number(result)


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


def _run_success_tests():
    tests = [
        ("двадцать пять плюс тринадцать", "тридцать восемь"),
        ("один плюс один", "два"),
        ("ноль плюс ноль", "ноль"),
        ("минус пять плюс три", "минус два"),
        ("пять минус минус один", "шесть"),
        ("пять плюс два умножить на три минус один", "десять"),
        ("скобка открывается пять плюс два скобка закрывается умножить на три минус один", "двадцать"),
        ("два в степени четыре", "шестнадцать"),
        ("ноль в степени ноль", "один"),
        ("пять остаток от деления три", "два"),
        ("два умножить на три плюс четыре умножить на пять", "двадцать шесть"),
        ("сорок один и тридцать одна сотая разделить на семнадцать", "два и сорок три сотых"),
        ("девятнадцать и восемьдесят две сотых разделить на девяносто девять", "ноль и двадцать сотых и ноль два в периоде"),
        ("одна сотая", "ноль и одна сотая"),
        ("пять десятых", "ноль и пять десятых"),
        ("пять и пять десятых", "пять и пять десятых"),
        ("синус от пи разделить на четыре", ("ноль и семьсот семь тысячных", "ноли и семьсот семь тысячных")),
    ]

    passed = 0
    failed = 0
    for i, (text, expected) in enumerate(tests, 1):
        expected_str = expected if isinstance(expected, str) else expected[0]
        try:
            result = calc(text)
        except CalculatorError as e:
            print(f"[FAIL] {i:2d}. {text}")
            print(f"       ожидалось: {expected_str}")
            print(f"       получено:  ошибка '{e.message}'")
            failed += 1
            continue
        except Exception as e:
            print(f"[FAIL] {i:2d}. {text}")
            print(f"       непредвиденная ошибка: {e}")
            failed += 1
            continue

        ok = (result == expected) if isinstance(expected, str) else (result in expected)
        if ok:
            print(f"[ OK ] {i:2d}. {text} -> {result}")
            passed += 1
        else:
            print(f"[FAIL] {i:2d}. {text}")
            print(f"       ожидалось: {expected_str}")
            print(f"       получено:  {result}")
            failed += 1

    return passed, failed


def _run_error_tests():
    tests = [
        ("пять разделить на ноль", DivisionByZeroError),
        ("пять остаток от деления ноль", ModuloByZeroError),
        ("скобка открывается пять плюс два", BracketBalanceError),
        ("пять плюс", InvalidSequenceError),
        ("десять один плюс два", InvalidNumberError),
        ("блабла плюс три", UnknownWordError),
        ("пять плюс плюс", InvalidSequenceError),
        ("ноль в степени минус один", ZeroToNegativePowerError),
        ("тангенс от пи разделить на два", TrigonometricUndefinedError),
        ("скобка открывается скобка закрывается", BracketNestingError),
    ]

    passed = 0
    failed = 0
    for i, (text, expected_class) in enumerate(tests, 1):
        try:
            result = calc(text)
        except expected_class as e:
            print(f"[ OK ] {i:2d}. {text} -> ошибка '{e.message}'")
            passed += 1
            continue
        except CalculatorError as e:
            print(f"[FAIL] {i:2d}. {text}")
            print(f"       ожидалось: {expected_class.__name__}")
            print(f"       получено:  {type(e).__name__}: {e.message}")
            failed += 1
            continue
        except Exception as e:
            print(f"[FAIL] {i:2d}. {text}")
            print(f"       непредвиденная ошибка: {e}")
            failed += 1
            continue
        print(f"[FAIL] {i:2d}. {text}")
        print(f"       ожидалась ошибка {expected_class.__name__}, получено {result}")
        failed += 1

    return passed, failed


def run_tests():
    print("=" * 60)
    print("Успешные тесты")
    print("=" * 60)
    p1, f1 = _run_success_tests()
    print()
    print("=" * 60)
    print("Тесты на ошибки")
    print("=" * 60)
    p2, f2 = _run_error_tests()
    print()
    print("=" * 60)
    total_pass = p1 + p2
    total_fail = f1 + f2
    print(f"Итого: прошло {total_pass}, упало {total_fail}")
    print("=" * 60)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("test", "--test", "-t"):
        run_tests()
    else:
        interactive()