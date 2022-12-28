from random import randint, choice

RULE = "What is the result of the expression?"


def calc():
    numb_1 = randint(1, 30)
    numb_2 = randint(1, 30)
    sign = choice("+-*")
    if sign == "+":
        right_answer = numb_1 + numb_2
    if sign == "-":
        right_answer = numb_1 - numb_2
    if sign == "*":
        right_answer = numb_1 * numb_2
    question = str(numb_1) + " " + sign + " " + str(numb_2)
    return (str(right_answer), question)


get_round_data = calc
