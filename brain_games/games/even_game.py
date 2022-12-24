from random import randint


def even():
    numb = randint(1, 30)
    question = "Question: " + str(numb)
    if numb % 2 == 0:
        right = "yes"
    else:
        right = "no"
    return (right, question)
