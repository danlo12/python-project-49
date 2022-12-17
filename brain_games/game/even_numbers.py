import prompt
from random import randint


def quest():
   numb = randint(1, 30)
   question = "Question: " + str(numb)
   print(question)
   answer = prompt.string("Your answer:")
   if numb % 2 == 0:
      right = "yes"
   else:
      right = "no"
   if answer == right:
      return ("right",)
   if answer != right:
      error = answer + " is wrong answer ;(. Correct answer was " + right
      return ("error", error)
