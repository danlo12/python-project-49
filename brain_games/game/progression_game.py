import prompt
from random import randint


def progress():
   numb_1 = randint(1, 30)
   numb_2 = randint(0, 9)
   numb_3 = randint(1, 5)
   timer = 10
   quest = [str(numb_1),]
   while timer > 0:
      numb_1 += numb_3
      quest.append(str(numb_1))
      timer -= 1
   right = quest[numb_2]
   quest[numb_2] = ".."
   question = "Question: " + quest[0] + " " + quest[1] + " "  + quest[2] + " " + quest[3] + " " + quest[4] + " " + quest[5] + " " + quest[6] + " " + quest[7] + " " + quest[8] + " " + quest[9]
   print(question)
   answer = prompt.string("Your answer:")
   if answer == right:
      return ("right",)
   if answer != right:
      error = answer + " is wrong answer ;(. Correct answer was " + right
      return ("error", error)

