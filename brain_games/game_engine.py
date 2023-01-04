import prompt


def game(module):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(module.RULE)
    step = ""
    timer_1 = "123"
    for step in timer_1:
        right, question = module.get_round_data()
        print(f"Question: {question}")
        answer = prompt.string("Your answer:")
        if answer != right:
            print(f"{answer} is wrong answer ;(. Correct answer was {right}")
            print(f"Let's try again, {name}!")
            break
        print("Correct!")
    else:
        print(f"Congratulations, {name}!")
