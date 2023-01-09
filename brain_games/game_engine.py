import prompt

ROUNDS_COUNT = 3


def run(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game.RULE)
    for _ in range(ROUNDS_COUNT):
        right_answer, question = game.get_round_data()
        print(f"Question: {question}")
        answer = prompt.string("Your answer:")
        if answer != right_answer:
            center = "is wrong answer ;(. Correct answer was"
            print(f"{answer} {center} {right_answer}")
            print(f"Let's try again, {name}!")
            break
        print("Correct!")
    else:
        print(f"Congratulations, {name}!")
