import prompt


def game(module):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(module.RULE)
    timer = 0
    while timer < 3:
        right, question = module.get_round_data()
        print(f"Question: {question}")
        answer = prompt.string("Your answer:")
        if answer == right:
            print("Correct!")
        elif answer != right:
            print(f"{answer} is wrong answer ;(. Correct answer was {right}")
            print(f"Let's try again, {name}!")
            break
        if timer == 2:
            print(f"Congratulations, {name}!")
            break
        timer += 1
