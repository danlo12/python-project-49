import prompt
from random import randint
from math import gcd


def gcd_g():
    numb_1 = randint(1, 30)
    numb_2 = randint(1, 30)
    question = "Question: " + str(numb_1) + " " + str(numb_2)
    print(question)
    answer = prompt.integer("Your answer:")
    right = gcd(numb_1, numb_2)
    center = " is wrong answer ;(. Correct answer was "
    error = str(answer) + center + str(gcd(numb_1, numb_2))
    return (answer, right, error)
