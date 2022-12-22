from brain_games.cli import welcome_user


def engine(func, rules):
    print("Welcome to the Brain Games!")
    name = welcome_user()
    timer = 0
    print(rules)
    while timer < 3:
        game = func()
        if game[0] == game[1]:
            print("Correct!")
        elif game[0] != game[1]:
            print(game[2])
            print("Let's try again, " + name + "!")
            break
        if timer == 2:
            print("Congratulations, " + name + "!")
            break
        timer += 1
