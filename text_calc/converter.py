from tokens import *


numerators = {
    "ноль": 0,
    "один": 1,
    "два": 2,
    "три": 3,
    "четыре": 4,
    "пять": 5,
    "шесть": 6,
    "семь": 7,
    "восемь": 8,
    "девять": 9,
    "десять": 10,
    "одиннадцать": 11,
    "двенадцать": 12,
    "тринадцать": 13,
    "четырнадцать": 14,
    "пятнадцать": 15,
    "шестнадцать": 16,
    "семнадцать": 17,
    "восемнадцать": 18,
    "девятнадцать": 19,
    "двадцать": 20,
    "тридцать": 30,
    "сорок": 40,
    "пятьдесят": 50,
    "шестьдесят": 60,
    "семьдесят": 70,
    "восемьдесят": 80,
    "девяносто": 90,
}

denominators = {
    "десятая": 10,
    "десятых": 10,
    "сотая": 100,
    "сотых": 100,
    "тысячная": 1000,
    "тысячных": 1000,
    "десятитысячная": 10000,
    "десятитысячных": 10000,
    "стотысячная": 100000,
    "стотысячных": 100000,
    "миллионная": 1000000,
    "миллионных": 1000000
}


operators = {
    "плюс": ADD,
    "и": ADD,
    "прибавить": ADD,
    "сложить": ADD,
    "сложить с": ADD,

    "минус": SUB,
    "вычесть": SUB,
    "отнять": SUB,

    "на": MUL,
    "умножить": MUL,
    "умножить на": MUL,
    "перемножить": MUL,

    "разделить": DIV,
    "разделить на": DIV,
    "поделить": DIV,
    "поделить на": DIV,
    "делить": DIV,
    "делить на": DIV,
    "дробь": DIV,

    "в": POW,
    "в степени": POW,
    "возвести в степень": POW,
    "возвести": POW,

    "синус": SIN,
    "синус от": SIN,

    "косинус": COS,
    "косинус от ": COS,

    "тангенс": TAN,
    "тангенс от": TAN
}

open_brackets = {
    "открывающая скобка": OPEN,
    "открывающаяся скобка": OPEN,
    "скобка открывается": OPEN,
    "открыть скобку": OPEN
}

close_brackets = {
    "закрывающая скобка": CLOSE,
    "закрывающаяся скобка": CLOSE,
    "скобка закрывается": CLOSE,
    "закрыть скобку": CLOSE
}


# NUMERATOR, DENOMINATOR, OPERATOR и т.д. из tokens
def get_object_info(word): # возвращает кортеж (тип, значение)
    if word in numerators:
        return NUMERATOR, numerators[word]
    if word in denominators:
        return DENOMINATOR, denominators[word]
    if word in operators:
        return OPERATOR, operators[word]
    if word in open_brackets:
        return OPEN_BRACKET, open_brackets[word]
    if word in close_brackets:
        return CLOSE_BRACKET, close_brackets[word]

    return None, None




    

