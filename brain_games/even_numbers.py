import prompt
from random import randint


def quest():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    timer = 0
    while timer < 3:
       numb = randint(1, 20)
       print("Question: " + str(numb))
       answer = prompt.string("Your answer: ")
       if answer == 'yes':
          if numb % 2 == 0:
             print("Correct!")
             if timer == 2:
                print("Congratulations, " + name)
                break
          else:
             print("Let's try again, " + name)
             break
       elif answer == 'no':
          if numb % 2 == 0:
             print("Let's try again, " + name)
             break
          else:
             print("Correct!")
             if timer == 2:
                print("Congratulations, " + name)
                break
       else:
          print("Let's try again, " + name)
          break
       timer += 1
