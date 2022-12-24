import prompt


def run_game(func, rules):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    timer = 0
    print(rules)
    while timer < 3:
        game = func()
        question = game[1]
        right = game[0]
        print(question)
        answer = prompt.string("Your answer:")
        if answer == right:
            print("Correct!")
        elif answer != right:
            print(answer + " is wrong answer ;(. Correct answer was " + right)
            print("Let's try again, " + name + "!")
            break
        if timer == 2:
            print("Congratulations, " + name + "!")
            break
        timer += 1
