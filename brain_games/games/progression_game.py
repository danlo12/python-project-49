from random import randint

RULE = 'What number is missing in the progression?'


def progress():
    numb_1 = randint(1, 30)
    numb_2 = randint(0, 9)
    numb_3 = randint(1, 5)
    timer = 10
    progression_list = [str(numb_1), ]
    while timer > 0:
        numb_1 += numb_3
        progression_list.append(str(numb_1))
        timer -= 1
    right_answer = progression_list[numb_2]
    progression_list[numb_2] = ".."
    separator = ' '
    question = separator.join(progression_list)
    return (right_answer, question)


get_round_data = progress
