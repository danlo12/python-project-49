from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(numb):
    check = 2
    if numb == 2:
        return True
    while numb % check != 0:
        check += 1
    if check == numb:
        return True
    else:
        return False


def get_round_data():
    numb = randint(2, 53)
    if is_prime(numb) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = str(numb)
    return (right_answer, question)
