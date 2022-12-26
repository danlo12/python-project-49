from random import randint

rule = 'What number is missing in the progression?'


def progress():
    numb_1 = randint(1, 30)
    numb_2 = randint(0, 9)
    numb_3 = randint(1, 5)
    timer = 10
    quest = [str(numb_1), ]
    while timer > 0:
        numb_1 += numb_3
        quest.append(str(numb_1))
        timer -= 1
    right = quest[numb_2]
    quest[numb_2] = ".."
    question = "Question: "
    timer_2 = 0
    while timer_2 <= 9:
        question = question + quest[timer_2] + " "
        timer_2 += 1
    return (right, question)


func = progress
