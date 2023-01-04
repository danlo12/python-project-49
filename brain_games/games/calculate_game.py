from random import randint, choice

RULE = "What is the result of the expression?"


def get_round_data():
    numb_1 = randint(1, 30)
    numb_2 = randint(1, 30)
    random_operator = choice("+-*")
    if random_operator == "+":
        right_answer = numb_1 + numb_2
    if random_operator == "-":
        right_answer = numb_1 - numb_2
    if random_operator == "*":
        right_answer = numb_1 * numb_2
    question = f"{str(numb_1)} {random_operator} {str(numb_2)}"
    return (str(right_answer), question)
