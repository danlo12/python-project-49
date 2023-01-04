from random import randint
from math import gcd

RULE = "Find the greatest common divisor of given numbers."


def get_round_data():
    numb_1 = randint(1, 30)
    numb_2 = randint(1, 30)
    question = f"{str(numb_1)} {str(numb_2)}"
    right_answer = gcd(numb_1, numb_2)
    return (str(right_answer), question)
