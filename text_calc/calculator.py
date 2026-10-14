import normalize
from tokenizer import tokenize
from tokens import *
from parser import to_reverse_polish_notation
from evaluator import calculate
from formatter import to_words_format

def calc(text):
    text = normalize.normalize(text)
    expression_list = tokenize(text) # все числа в формате дроби. в Эвуаляторе деление происходит последней операцией
    for x in expression_list:
        if type(x) is Number:
            print(x.value, end=" ")
        elif type(x) is Operator:
            print(x.operator, end=" ")
        elif type(x) is OpenedParen:
            print("(", end=" ")
        elif type(x) is ClosedParen:
            print(")", end=" ")
    rpn_expression_list = to_reverse_polish_notation(expression_list)
    answer = calculate(rpn_expression_list)
    print("=", answer)
    #answer_words = to_words_format(answer)
    #print(answer_words)
    for x in rpn_expression_list:
        if type(x) is Number:
            print(x.value, end=" ")
        elif type(x) is Operator:
            print(x.operator, end=" ")
        elif type(x) is OpenedParen:
            print("(", end=" ")
        elif type(x) is ClosedParen:
            print(")", end=" ")
    print("\n------------------------------------")


a = "два в степени два возвести в степень три"
calc(a)
a = "минус минус минус три плюс минус минус два умножить четыре"
calc(a)
a = "два минус минус три"
calc(a)
#a = "два делить на ноль"
#calc(a)
a = "два плюс минус три"
calc(a)
a = "два плюс скобка открывается четыре умножить на три минус скобка открывается двадцать пять делить на пять в степени пять скобка закрывается скобка закрывается в степени три минус четыре"
calc(a)
#a = "два в степени три в степени двадцать умножить на три минус пять в степени два в степени три в степени пять в степени восемь"
#calc(a)
##a = "скобка открывается сто четыре минус шестьдесят семь скобка закрывается в степени пятьдесят два в степени сорок два минус три"
calc(a)
a = "открытая скобка сто тридцать четыре минус два закрытая скобка умножить на сорок восемь плюс тринадцать в степени два делить на пять"
calc(a)

a = "двести пятьдесят плюс семь умножить на девять минус сорок два делить на шесть"
calc(a)

a = "открытая скобка восемьдесят восемь плюс двенадцать закрытая скобка делить на двадцать пять минус три в степени три"
calc(a)

a = "девятьсот девяносто девять минус пятьсот шестьдесят семь плюс восемь умножить на четыре"
calc(a)

a = "открытая скобка сорок пять минус пятнадцать закрытая скобка умножить на открытая скобка шесть плюс четыре закрытая скобка"
calc(a)

a = "девяносто девять делить на три плюс семнадцать умножить на два минус пять в степени два"
calc(a)

a = "открытая скобка двести минус сто двадцать закрытая скобка умножить на три плюс сорок восемь делить на восемь"
calc(a)

a = "шестьдесят четыре делить на восемь плюс открытая скобка тридцать минус семь закрытая скобка умножить на два"
calc(a)

a = "пятьсот пятьдесят пять минус открытая скобка двести десять плюс девяносто закрытая скобка делить на три"
calc(a)

a = "открытая скобка семь плюс восемь закрытая скобка умножить на открытая скобка девять минус четыре закрытая скобка плюс два в степени четыре"
calc(a)
