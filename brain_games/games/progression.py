from random import randint

RULE = 'What number is missing in the progression?'


def get_round_data():
    start = randint(1, 30)
    step = randint(0, 9)
    random_index = randint(1, 5)
    timer = 10
    progression_list = [str(start), ]
    while timer > 0:
        start += random_index
        progression_list.append(str(start))
        timer -= 1
    right_answer = progression_list[step]
    progression_list[step] = ".."
    question = " ".join(progression_list)
    return (right_answer, question)
