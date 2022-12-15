import prompt
from brain_games.game.cli import welcome_user
from brain_games.game.even_numbers import quest
from brain_games.game.calculate_game import calc
from brain_games.game.gcd_game import gcd_g

def engine(check, rules):
    name = welcome_user()
    timer = 0
    print(rules)
    while timer < 3:
       if check == 1:
          func = quest()
       if check == 2:
          func = calc()
       if check == 3:
          func = gcd_g()
       if func[0] == "right":
          print("Correct!")
       elif func[0] == "error":
          print(func[1])
          print("Let's try again, " + name)
          break
       if timer == 2:
          print("Congratulations, " + name)
          break
       timer += 1
