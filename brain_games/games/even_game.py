from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    numb = randint(1, 30)
    question = str(numb)
    if numb % 2 == 0:
        right_answer = "yes"
    else:
        right_answer = "no"
    return (right_answer, question)


get_round_data = even
