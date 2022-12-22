import prompt
from random import randint


def even():
    numb = randint(1, 30)
    question = "Question: " + str(numb)
    print(question)
    answer = prompt.string("Your answer:")
    if numb % 2 == 0:
        right = "yes"
    else:
        right = "no"
    error = answer + " is wrong answer ;(. Correct answer was " + right
    return (answer, right, error)
