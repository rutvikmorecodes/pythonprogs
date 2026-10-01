"""Project 2: Number Guessing Game

Store a secret number.
Ask the user to guess it.
Tell the user whether the guess is too high or too low.
Continue until the correct number is guessed.
Count the number of attempts.

"""
import random
num = random.randint(1,100)


def cc(num,guess):
       if num == guess:
          print(f" perfect , correct number is  : {guess} ")
          return True
       elif num > guess:
          print("number is greater ")
          return False
       else:
         print("number is lower ")
         return False
       


for i in range(1,100):
    guess = int(input("guess the number  between 1 to 100 "))
    if cc(num,guess):
        print(f"you got in {i} numbers of attemt ")
        break