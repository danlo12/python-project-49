from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def primality_check(numb):
    right_answer = 'no'
    check = 2
    if numb == 2:
        right_answer = 'yes'
    while numb % check != 0:
        check += 1
    if check == numb:
        right_answer = 'yes'
    return right_answer


def prime():
    numb = randint(2, 53)
    right_answer = primality_check(numb)
    question = str(numb)
    return (right_answer, question)


get_round_data = prime
