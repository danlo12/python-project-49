from random import randint
from math import gcd

RULE = "Find the greatest common divisor of given numbers."


def gcd_g():
    numb_1 = randint(1, 30)
    numb_2 = randint(1, 30)
    question = str(numb_1) + " " + str(numb_2)
    right_answer = gcd(numb_1, numb_2)
    return (str(right_answer), question)


get_round_data = gcd_g
