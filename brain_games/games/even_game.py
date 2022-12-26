from random import randint

rule = 'Answer "yes" if the number is even, otherwise answer "no"'


def even():
    numb = randint(1, 30)
    question = "Question: " + str(numb)
    if numb % 2 == 0:
        right = "yes"
    else:
        right = "no"
    return (right, question)


func = even
