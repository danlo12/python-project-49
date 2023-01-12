from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(numb):
    step_count = numb + 1
    for _ in range(step_count):
        if numb % _ == 0 and numb != _ and _ != 1:
            return False
        elif numb == _:
            return True


def get_round_data():
    numb = randint(1, 53)
    if is_prime(numb):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (right_answer, numb)
