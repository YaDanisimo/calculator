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
    
Так же можно писать такую проверку:
if isinstance(token, (Operator, OpenBracket)):
    print("Это оператор или открывающаяся скобка")

Так же существует наследование: 
token = Add()
isinstance(token, Add) -> True
isinstance(token, Operator) -> True -- т.к. Add наследуется от Operator
isinstance(token, Pow) -> False
Так же функции и другие операторы наследуются от Operator 
 
Я в тебя верю.
'''


# Это то, что надо сделать.
# Если задача большая, то раздели её на несколько функций
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

def ans(rpn_expression):
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
    return " ".join(ans)

def run_test(test_num, tokens, correct_str):
    result = to_rpn(tokens)
    result_str = ans(result)
    print(f"Тест {test_num}:")
    print(f"Результат: {result_str}")
    print(f"Ответ:     {correct_str}")
    print(f"Совпало:   {result_str == correct_str}")
    print("----------------")

# --- ТЕСТЫ ---

tokens1 = [Number(2), Add(), Number(3)]
run_test(1, tokens1, "2 3 +")

tokens2 = [Number(5), Sub(), Number(2)]
run_test(2, tokens2, "5 2 -")

tokens3 = [Number(4), Mul(), Number(5)]
run_test(3, tokens3, "4 5 *")

tokens4 = [Number(10), Div(), Number(2)]
run_test(4, tokens4, "10 2 :")

tokens5 = [Number(2), Pow(), Number(3)]
run_test(5, tokens5, "2 3 **")

tokens6 = [Sin(), Number(30)]
run_test(6, tokens6, "30 sin")

tokens7 = [Cos(), Number(60)]
run_test(7, tokens7, "60 cos")

tokens8 = [Tan(), Number(45)]
run_test(8, tokens8, "45 tan")

tokens9 = [UnarySub(), Number(5)]
run_test(9, tokens9, "5 u-")

tokens10 = [Number(1, 2), Add(), Number(1, 3)]
run_test(10, tokens10, "1/2 1/3 +")

tokens11 = [Number(1), Add(), Number(2), Mul(), Number(3)]
run_test(11, tokens11, "1 2 3 * +")

tokens12 = [OpenBracket(), Number(1), Add(), Number(2), CloseBracket(), Mul(), Number(3)]
run_test(12, tokens12, "1 2 + 3 *")

tokens13 = [Number(2), Pow(), Number(3), Pow(), Number(2)]
run_test(13, tokens13, "2 3 2 ** **")

tokens14 = [Number(10), Sub(), Number(5), Sub(), Number(2)]
run_test(14, tokens14, "10 5 - 2 -")

tokens15 = [Sin(), OpenBracket(), Number(30), CloseBracket(), Add(), Number(5)]
run_test(15, tokens15, "30 sin 5 +")

tokens16 = [Number(2), Mul(), OpenBracket(), Number(3), Add(), Number(4), CloseBracket()]
run_test(16, tokens16, "2 3 4 + *")

tokens17 = [UnarySub(), OpenBracket(), Number(3), Add(), Number(2), CloseBracket(), Mul(), Number(4)]
run_test(17, tokens17, "3 2 + u- 4 *")

tokens18 = [Number(1, 2), Mul(), Number(2, 3)]
run_test(18, tokens18, "1/2 2/3 *")

tokens19 = [Cos(), OpenBracket(), Number(60), Mul(), Number(2), CloseBracket()]
run_test(19, tokens19, "60 2 * cos")

tokens20 = [Number(2), Pow(), OpenBracket(), Number(3), Add(), Number(1), CloseBracket()]
run_test(20, tokens20, "2 3 1 + **")

tokens21 = [OpenBracket(), UnarySub(), Number(5), CloseBracket(), Pow(), Number(2)]
run_test(21, tokens21, "5 u- 2 **")

tokens22 = [Number(10), Div(), OpenBracket(), Number(2), Add(), Number(3), CloseBracket()]
run_test(22, tokens22, "10 2 3 + :")

tokens23 = [Sin(), OpenBracket(), Cos(), OpenBracket(), Number(0), CloseBracket(), CloseBracket()]
run_test(23, tokens23, "0 cos sin")

tokens24 = [Number(5), Pow(), Number(2), Sub(), Number(3), Mul(), Number(2)]
run_test(24, tokens24, "5 2 ** 3 2 * -")

tokens25 = [OpenBracket(), Number(1), Add(), Number(2), CloseBracket(), Div(), OpenBracket(), Number(3), Sub(), Number(1), CloseBracket()]
run_test(25, tokens25, "1 2 + 3 1 - :")

# --- СЛОЖНЫЕ ТЕСТЫ (от 10 токенов) ---

tokens26 = [Number(2), Add(), Number(3), Mul(), OpenBracket(), Number(4), Sub(), Number(5), CloseBracket(), Pow(), Number(2), Div(), Number(6)]
run_test(26, tokens26, "2 3 4 5 - 2 ** * 6 : +")

tokens27 = [UnarySub(), Sin(), OpenBracket(), Number(30), CloseBracket(), Add(), Cos(), OpenBracket(), Number(60), CloseBracket(), Mul(), Tan(), OpenBracket(), Number(45), CloseBracket()]
run_test(27, tokens27, "30 sin u- 60 cos 45 tan * +")

tokens28 = [UnarySub(), OpenBracket(), Number(2), Add(), Number(3), CloseBracket(), Pow(), Number(2), Sub(), Number(4), Mul(), OpenBracket(), Number(5), Add(), Number(6), CloseBracket()]
run_test(28, tokens28, "2 3 + u- 2 ** 4 5 6 + * -")

tokens29 = [Number(1, 2), Mul(), OpenBracket(), Number(3, 4), Add(), Number(5, 6), CloseBracket(), Sub(), Number(7, 8)]
run_test(29, tokens29, "1/2 3/4 5/6 + * 7/8 -")

tokens30 = [Sin(), OpenBracket(), Number(30), Add(), Number(60), CloseBracket(), Mul(), Cos(), OpenBracket(), Number(45), CloseBracket(), Sub(), Tan(), OpenBracket(), Number(90), Div(), Number(2), CloseBracket()]
run_test(30, tokens30, "30 60 + sin 45 cos * 90 2 : tan -")