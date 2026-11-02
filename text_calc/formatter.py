from converter import (
    number_to_word,
    number_to_word_feminine,
    hundreds_to_word,
    denominator_to_words,
)


def _decimal_expansion(num, den, max_digits=10):
    digits = []
    seen = {}
    rem = num
    while rem != 0 and rem not in seen and len(digits) < max_digits:
        seen[rem] = len(digits)
        rem *= 10
        digits.append(rem // den)
        rem %= den
    if rem == 0:
        return digits, []
    if rem in seen:
        start = seen[rem]
        return digits[:start], digits[start:]
    return None, None


def to_format(num):
    numer = num.numerator
    denom = num.denominator

    def under_1000(n, feminine=False):
        result = []
        if n == 0:
            return ""
        if n >= 100:
            result.append(hundreds_to_word[(n // 100) * 100])
            n %= 100
        if n >= 20:
            result.append(number_to_word[(n // 10) * 10])
            n %= 10
        if n > 0:
            if feminine and n in number_to_word_feminine:
                result.append(number_to_word_feminine[n])
            else:
                result.append(number_to_word[n])
        return " ".join(result)

    def integer_to_words(n, feminine=False):
        if n == 0:
            return number_to_word[0]
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

    def fraction_words(n, d):
        last_two = n % 100
        last_one = n % 10
        form = 0 if (last_one == 1 and last_two != 11) else 1
        return f"{integer_to_words(n, feminine=True)} {denominator_to_words[d][form]}"

    def format_rounded():
        q, r = divmod(numer * 1000, denom)
        if r * 2 >= denom:
            q += 1
        int_part_r = q // 1000
        frac_part_r = q % 1000
        if frac_part_r == 0:
            return integer_to_words(int_part_r)
        return f"{integer_to_words(int_part_r)} и {fraction_words(frac_part_r, 1000)}"

    sign = "минус " if numer < 0 else ""
    numer = abs(numer)

    if denom == 1:
        return sign + integer_to_words(numer)

    integer_part = numer // denom
    fractional_part = numer % denom

    pre_digits, period_digits = _decimal_expansion(fractional_part, denom, max_digits=10)

    if pre_digits is None:
        return sign + format_rounded()

    if period_digits and len(period_digits) > 4:
        return sign + format_rounded()

    value = []
    if integer_part > 0:
        value.append(integer_to_words(integer_part))
        value.append("и")
    elif pre_digits or period_digits:
        value.append(number_to_word[0])
        value.append("и")

    if pre_digits:
        pre_val = 0
        for d in pre_digits:
            pre_val = pre_val * 10 + d
        pre_den = 10 ** len(pre_digits)
        if pre_den not in denominator_to_words:
            return sign + format_rounded()
        value.append(fraction_words(pre_val, pre_den))

    if period_digits:
        if pre_digits:
            value.append("и")
        value.append(" ".join(number_to_word[d] for d in period_digits))
        value.append("в периоде")

    if not value:
        return sign + number_to_word[0]

    return sign + " ".join(value)


format_number = to_format