from random import randint


def prime():
    numb = randint(2, 53)
    check = 2
    right = 'no'
    if numb == 2:
        right = 'yes'
    while numb % check != 0:
        check += 1
        if check == numb:
            right = 'yes'
    question = "Question: " + str(numb)
    return (right, question)
