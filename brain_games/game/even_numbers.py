import prompt
from random import randint


def quest():
   numb = randint(1, 30)
   question = "Question: " + str(numb)
   print(question)
   answer = prompt.string("Your answer:")
   if numb % 2 == 0:
      right = "yes"
      error = "'no' is wrong answer ;(. Correct answer was 'yes'."
   else:
      right = "no"
      error = "'yes' is wrong answer ;(. Correct answer was 'no'."
   if answer == right:
      return ("right", error)
   if answer != right:
      return ("error", error)
