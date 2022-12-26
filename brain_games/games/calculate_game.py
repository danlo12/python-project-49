from random import randint, choice

rule = "What is the result of the expression?"


def calc():
    numb_1 = randint(1, 30)
    numb_2 = randint(1, 30)
    sign = choice("+-*")
    if sign == "+":
        right = numb_1 + numb_2
    if sign == "-":
        right = numb_1 - numb_2
    if sign == "*":
        right = numb_1 * numb_2
    question = "Question: " + str(numb_1) + " " + sign + " " + str(numb_2)
    return (str(right), question)


func = calc
