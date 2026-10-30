from tokens import *

'''
Тебе даётся на вход список из токенов формата:
[Number, Add, Number, Number, OpenBracket, ...].

Number - число.

Add, Sub, UnarySub, Sin, Cos, Pow и тд (все в tokens.py) - операторы.
У операторов есть три своих переменных:
priority, association, is_unary. 
Обращаться к ним как token.priority, token.is_unary и тд, где obj - токен из tokens.
priority хранит числа от 1 до 3. Чем больше, тем выше приоритет оператора
association = LEFT или RIGHT. Да, прям LEFT или RIGHT. Очень удобно и читаемо
is_unary = True или False. Понятно, думаю

OpenBracket, CloseBracket ничего не хранят. Просто обозначения скобок.

Зачем все токены это классы?
их удобно сравнивать. Например есть токен token.
Мы можем сравнить его с классом Number
if isinstance(token, Number):
    print("это число")
    
так же можно писать такую проверку:
if isinstance(token, (Operator, OpenBracket)):
    print("Это оператор или открывающаяся скобка")
    
Я в тебя верю.
'''



def to_rpn(tokens) -> list:
    return []

# Для тестов. Переводит токены в символы
op_to_sym = {
    Add: "+",
    Sub: "-",
    UnarySub: "u-",
    Mul: "*",
    Div: ":",
    Pow: "**",
    Sin: "sin",
    Cos: "cos",
    Tan: "tan"
}

def print_ans(rpn_expression):
    ans = []
    for obj in rpn_expression:
        if isinstance(obj, Number):
            if obj.denominator is None or obj.denominator == 1:
                ans.append(str(obj.numerator))
            else:
                ans.append(f"{obj.numerator}/{obj.denominator}")
        elif isinstance(obj, Operator):
            ans.append(op_to_sym[type(obj)])
        elif isinstance(obj, OpenBracket):
            ans.append("(")
        elif isinstance(obj, CloseBracket):
            ans.append(")")
    print(*ans, sep=" ")


# --- ТЕСТЫ ---

tokens1 = [Number(2), Add(), Number(3)]
result1 = to_rpn(tokens1)
print_ans(result1)
# 2 3 +
print("----------------")

tokens2 = [Number(5), Sub(), Number(2)]
result2 = to_rpn(tokens2)
print_ans(result2)
# 5 2 -
print("----------------")

tokens3 = [Number(4), Mul(), Number(5)]
result3 = to_rpn(tokens3)
print_ans(result3)
# 4 5 *
print("----------------")

tokens4 = [Number(10), Div(), Number(2)]
result4 = to_rpn(tokens4)
print_ans(result4)
# 10 2 :
print("----------------")

tokens5 = [Number(2), Pow(), Number(3)]
result5 = to_rpn(tokens5)
print_ans(result5)
# 2 3 **
print("----------------")

tokens6 = [Sin(), Number(30)]
result6 = to_rpn(tokens6)
print_ans(result6)
# 30 sin
print("----------------")

tokens7 = [Cos(), Number(60)]
result7 = to_rpn(tokens7)
print_ans(result7)
# 60 cos
print("----------------")

tokens8 = [Tan(), Number(45)]
result8 = to_rpn(tokens8)
print_ans(result8)
# 45 tan
print("----------------")

tokens9 = [UnarySub(), Number(5)]
result9 = to_rpn(tokens9)
print_ans(result9)
# 5 u-
print("----------------")

tokens10 = [Number(1, 2), Add(), Number(1, 3)]
result10 = to_rpn(tokens10)
print_ans(result10)
# 1/2 1/3 +
print("----------------")

tokens11 = [Number(1), Add(), Number(2), Mul(), Number(3)]
result11 = to_rpn(tokens11)
print_ans(result11)
# 1 2 3 * +
print("----------------")

tokens12 = [OpenBracket(), Number(1), Add(), Number(2), CloseBracket(), Mul(), Number(3)]
result12 = to_rpn(tokens12)
print_ans(result12)
# 1 2 + 3 *
print("----------------")

tokens13 = [Number(2), Pow(), Number(3), Pow(), Number(2)]
result13 = to_rpn(tokens13)
print_ans(result13)
# 2 3 2 ** **
print("----------------")

tokens14 = [Number(10), Sub(), Number(5), Sub(), Number(2)]
result14 = to_rpn(tokens14)
print_ans(result14)
# 10 5 - 2 -
print("----------------")

tokens15 = [Sin(), OpenBracket(), Number(30), CloseBracket(), Add(), Number(5)]
result15 = to_rpn(tokens15)
print_ans(result15)
# 30 sin 5 +
print("----------------")

tokens16 = [Number(2), Mul(), OpenBracket(), Number(3), Add(), Number(4), CloseBracket()]
result16 = to_rpn(tokens16)
print_ans(result16)
# 2 3 4 + *
print("----------------")

tokens17 = [UnarySub(), OpenBracket(), Number(3), Add(), Number(2), CloseBracket(), Mul(), Number(4)]
result17 = to_rpn(tokens17)
print_ans(result17)
# 3 2 + u- 4 *
print("----------------")

tokens18 = [Number(1, 2), Mul(), Number(2, 3)]
result18 = to_rpn(tokens18)
print_ans(result18)
# 1/2 2/3 *
print("----------------")

tokens19 = [Cos(), OpenBracket(), Number(60), Mul(), Number(2), CloseBracket()]
result19 = to_rpn(tokens19)
print_ans(result19)
# 60 2 * cos
print("----------------")

tokens20 = [Number(2), Pow(), OpenBracket(), Number(3), Add(), Number(1), CloseBracket()]
result20 = to_rpn(tokens20)
print_ans(result20)
# 2 3 1 + **
print("----------------")

tokens21 = [OpenBracket(), UnarySub(), Number(5), CloseBracket(), Pow(), Number(2)]
result21 = to_rpn(tokens21)
print_ans(result21)
# 5 u- 2 **
print("----------------")

tokens22 = [Number(10), Div(), OpenBracket(), Number(2), Add(), Number(3), CloseBracket()]
result22 = to_rpn(tokens22)
print_ans(result22)
# 10 2 3 + :
print("----------------")

tokens23 = [Sin(), OpenBracket(), Cos(), OpenBracket(), Number(0), CloseBracket(), CloseBracket()]
result23 = to_rpn(tokens23)
print_ans(result23)
# 0 cos sin
print("----------------")

tokens24 = [Number(5), Pow(), Number(2), Sub(), Number(3), Mul(), Number(2)]
result24 = to_rpn(tokens24)
print_ans(result24)
# 5 2 ** 3 2 * -
print("----------------")

tokens25 = [OpenBracket(), Number(1), Add(), Number(2), CloseBracket(), Div(), OpenBracket(), Number(3), Sub(), Number(1), CloseBracket()]
result25 = to_rpn(tokens25)
print_ans(result25)
# 1 2 + 3 1 - :
print("----------------")

# --- СЛОЖНЫЕ ТЕСТЫ (от 10 токенов) ---

tokens26 = [Number(2), Add(), Number(3), Mul(), OpenBracket(), Number(4), Sub(), Number(5), CloseBracket(), Pow(), Number(2), Div(), Number(6)]
result26 = to_rpn(tokens26)
print_ans(result26)
# 2 3 4 5 - 2 ** * 6 : +
print("----------------")

tokens27 = [UnarySub(), Sin(), OpenBracket(), Number(30), CloseBracket(), Add(), Cos(), OpenBracket(), Number(60), CloseBracket(), Mul(), Tan(), OpenBracket(), Number(45), CloseBracket()]
result27 = to_rpn(tokens27)
print_ans(result27)
# 30 sin u- 60 cos 45 tan * +
print("----------------")

tokens28 = [UnarySub(), OpenBracket(), Number(2), Add(), Number(3), CloseBracket(), Pow(), Number(2), Sub(), Number(4), Mul(), OpenBracket(), Number(5), Add(), Number(6), CloseBracket()]
result28 = to_rpn(tokens28)
print_ans(result28)
# 2 3 + u- 2 ** 4 5 6 + * -
print("----------------")

tokens29 = [Number(1, 2), Mul(), OpenBracket(), Number(3, 4), Add(), Number(5, 6), CloseBracket(), Sub(), Number(7, 8)]
result29 = to_rpn(tokens29)
print_ans(result29)
# 1/2 3/4 5/6 + * 7/8 -
print("----------------")

tokens30 = [Sin(), OpenBracket(), Number(30), Add(), Number(60), CloseBracket(), Mul(), Cos(), OpenBracket(), Number(45), CloseBracket(), Sub(), Tan(), OpenBracket(), Number(90), Div(), Number(2), CloseBracket()]
result30 = to_rpn(tokens30)
print_ans(result30)
# 30 60 + sin 45 cos * 90 2 : tan -
print("----------------")