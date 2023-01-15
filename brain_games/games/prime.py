from random import randint
import math

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False

    for devider in range(2, int(math.sqrt(number) + 1)):
        if number % devider == 0:
            return False

    return True


def get_round_data():
    numb = randint(1, 53)
    if is_prime(numb):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (right_answer, numb)
