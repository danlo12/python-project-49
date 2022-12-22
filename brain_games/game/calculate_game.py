import prompt
from random import randint, choice


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
    print(question)
    answer = prompt.integer("Your answer:")
    center = " is wrong answer ;(. Correct answer was "
    error = str(answer) + center + str(right)
    return (answer, right, error)

