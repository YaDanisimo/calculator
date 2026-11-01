from tokens import *

"""

int -> str

вход: Number: numerator, denominator

"""

# denominators = {
#     10: "десятая",
#     100: "сотая",
#     1000: "тысячная",
#     10000: "десятитысячная",
#     100000: "стотысячная",
#     1000000: "миллионная",
# }

# operators = {
#     ADD: ["плюс", "и", "прибавить", "сложить", "сложить с"],
#     SUB: ["минус", "вычесть", "отнять"],
#     MUL: ["на", "умножить", "умножить на", "перемножить"],
#     DIV: ["разделить", "разделить на", "поделить", "поделить на",
#           "делить", "делить на", "дробь"],
#     POW: ["в", "в степени", "возвести в степень", "возвести"],
#     SIN: ["синус", "синус от"],
#     COS: ["косинус", "косинус от "],
#     TAN: ["тангенс", "тангенс от"],
# }

# ADD, SUB, MUL, DIV, POW, SIN, COS, TAN, OPEN, CLOSE = range(0, 10)


numerators = {
    0: "ноль",
    1: "один",
    2: "два",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять",
    10: "десять",
    11: "одиннадцать",
    12: "двенадцать",
    13: "тринадцать",
    14: "четырнадцать",
    15: "пятнадцать",
    16: "шестнадцать",
    17: "семнадцать",
    18: "восемнадцать",
    19: "девятнадцать",
    20: "двадцать",
    30: "тридцать",
    40: "сорок",
    50: "пятьдесят",
    60: "шестьдесят",
    70: "семьдесят",
    80: "восемьдесят",
    90: "девяносто",
    100: "сто"

}

hundreds = {
    100: "сто",
    200: "двести",
    300: "триста",
    400: "четыреста",
    500: "пятьсот",
    600: "шестьсот",
    700: "семьсот",
    800: "восемьсот",
    900: "девятьсот",
}

thousands = {
    1000: "одна тысяча",
    2000: "две тысячи",
    3000: "три тысячи",
    4000: "четыре тысячи",
    5000: "пять тысяч",
    6000: "шесть тысяч",
    7000: "семь тысяч",
    8000: "восемь тысяч",
    9000: "девять тысяч",
}

ten_thousands = {
    10000: "десять тысяч",
    20000: "двадцать тысяч",
    30000: "тридцать тысяч",
    40000: "сорок тысяч",
    50000: "пятьдесят тысяч",
    60000: "шестьдесят тысяч",
    70000: "семьдесят тысяч",
    80000: "восемьдесят тысяч",
    90000: "девяносто тысяч",
}

hundred_thousands = {
    100000: "сто тысяч",
    200000: "двести тысяч",
    300000: "триста тысяч",
    400000: "четыреста тысяч",
    500000: "пятьсот тысяч",
    600000: "шестьсот тысяч",
    700000: "семьсот тысяч",
    800000: "восемьсот тысяч",
    900000: "девятьсот тысяч",
}

fraction_numerators = {
    1: "одна",
    2: "две",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять",
}

denominators = {
    10: ["десятая", "десятых"],
    100: ["сотая", "сотых"],
    1000: ["тысячная", "тысячных"],
    10000: ["десятитысячная", "десятитысячных"],
    100000: ["стотысячная", "стотысячных"],
    1000000: ["миллионная", "миллионных"],
}



# def formatter(Number):
#     numer = Number.numerator
#     denom = Number.denominator
#     if denom == 1:
#         value = ''
#
#         if 0 <= numer <= 20 :
#             value += numerators[numer]
#         elif 21 <= numer <= 99:
#             value += numerators[(numer//10)*10] + ' ' + numerators[numer%10]
#         elif 101 <= numer <= 999:
#             value += hundreds[(numer//100)*100] + ' ' + numerators[((numer%100)//10)*10] + ' ' + numerators[numer%10]
#         print(value)

    # else:
# пиздарики
# def formatter(Num):
#     numer = Num.numerator
#     denom = Num.denominator
#
#     if denom == 1:
#         value = ''
#
#         if 0 <= numer <= 20:
#             value += numerators[numer]
#
#         elif 21 <= numer <= 99:
#             value += numerators[(numer // 10) * 10]
#             if numer % 10 != 0:
#                 value += ' ' + numerators[numer % 10]
#
#         elif 100 <= numer <= 999:
#             value += hundreds[(numer // 100) * 100]
#
#             remainder = numer % 100
#             if remainder >= 20:
#                 value += ' ' + numerators[(remainder // 10) * 10]
#                 if remainder % 10 != 0:
#                     value += ' ' + numerators[remainder % 10]
#             elif remainder > 0:
#                 value += ' ' + numerators[remainder]
#
#         elif 1000 <= numer <= 999999:
#             thousands_part = numer // 1000
#             remainder = numer % 1000
#             if thousands_part <= 20:
#                 value += numerators[thousands_part]
#
#             elif thousands_part < 100:
#                 value += numerators[(thousands_part // 10) * 10]
#                 if thousands_part % 10 != 0:
#                     value += ' ' + numerators[thousands_part % 10]
#
#             else:
#                 value += hundreds[(thousands_part // 100) * 100]
#                 rest = thousands_part % 100
#                 if rest >= 20:
#                     value += ' ' + numerators[(rest // 10) * 10]
#                     if rest % 10 != 0:
#                         value += ' ' + numerators[rest % 10]
#                 elif rest > 0:
#                     value += ' ' + numerators[rest]
#
#             last_two = thousands_part % 100
#             last_one = thousands_part % 10
#
#             if 11 <= last_two <= 14:
#                 value += ' тысяч'
#
#             elif last_one == 1:
#                 value += ' тысяча'
#
#             elif 2 <= last_one <= 4:
#                 value += ' тысячи'
#
#             else:
#                 value += ' тысяч'
#
#             if remainder:
#                 if remainder >= 100:
#                     value += ' ' + hundreds[(remainder // 100) * 100]
#                 rest = remainder % 100
#                 if rest >= 20:
#                     value += ' ' + numerators[(rest // 10) * 10]
#                     if rest % 10 != 0:
#                         value += ' ' + numerators[rest % 10]
#                 elif rest > 0:
#                     value += ' ' + numerators[rest]
#
#         # print(value)
#     else:
#         value = ''
#         integer_part = numer // denom
#         fractional_part = numer % denom
#
#         if integer_part > 0:
#             value += formatter(Number(integer_part, 1))
#
#         if fractional_part > 0:
#             if value:
#                 value += ' и '
#             value += formatter(Number(fractional_part, 1))
#             if fractional_part == 1:
#                 value = value.replace('один', 'одна')
#             elif fractional_part == 2:
#                 value = value.replace('два', 'две')
#
#             last_two = fractional_part % 100
#             last_one = fractional_part % 10
#
#             if last_two == 1:
#                 form = 0
#             elif 2 <= last_two <= 4:
#                 form = 1
#             else:
#                 form = 1
#             value += ' ' + denominators[denom][form]
#
#         return value

def formatter(num):
    numer = num.numerator
    denom = num.denominator

    if not isinstance(numer, int) or not isinstance(denom, int):
        raise TypeError("Числитель и знаменатель должны быть целыми числами")
    if denom <= 0:
        raise ValueError("Знаменатель должен быть положительным")
    if denom != 1 and denom not in denominators:
        raise ValueError("Такой знаменатель не поддерживается")

    def under_1000(n, feminine=False):
        result = []
        if n == 0:
            return ""
        if n >= 100:
            result.append(hundreds[(n // 100) * 100])
            n %= 100
        if n >= 20:
            result.append(numerators[(n // 10) * 10])
            n %= 10
        if n > 0:
            if feminine and n == 1:
                result.append("одна")
            elif feminine and n == 2:
                result.append("две")
            else:
                result.append(numerators[n])

        return " ".join(result)

    def integer_to_words(n, feminine=False):
        if n == 0:
            return numerators[0]
        if n > 999999:
            raise ValueError("Поддерживаются числа не больше 999999")
        result = []

        thousands_part = n // 1000
        remainder = n % 1000
        if thousands_part > 0:
            result.append(under_1000(thousands_part, feminine=True))

            last_two = thousands_part % 100
            last_one = thousands_part % 10

            if 11 <= last_two <= 14:
                result.append("тысяч")
            elif last_one == 1:
                result.append("тысяча")
            elif 2 <= last_one <= 4:
                result.append("тысячи")
            else:
                result.append("тысяч")

        if remainder > 0:
            result.append(under_1000(remainder, feminine=feminine))
        return " ".join(result)

    sign = "минус " if numer < 0 else ""
    numer = abs(numer)

    if denom == 1:
        return sign + integer_to_words(numer)

    integer_part = numer // denom
    fractional_part = numer % denom
    value = []
    if integer_part > 0:
        value.append(integer_to_words(integer_part))
    if fractional_part > 0:
        fraction_words = integer_to_words(fractional_part,feminine=True)

        last_two = fractional_part % 100
        last_one = fractional_part % 10

        if last_one == 1 and last_two != 11:
            form = 0
        else:
            form = 1

        denominator_word = denominators[denom][form]
        value.append("и" if integer_part > 0 else "")
        value.append(fraction_words)
        value.append(denominator_word)
    if not value:
        return numerators[0]

    return sign + " ".join(word for word in value if word)


print(formatter(Number(154659,1)))




