#Brian Tong
#btong1@ucsc.edu
#programming assignment 1
#program randomizes a number from 1 to 10 and the user has 3 tries to guess the value correctly

import random

def guess():
  print("I'm thinking of an integer, you have three guesses.")
  x = random.randint(1,10)
  for j in range(3):
    print("Guess", j + 1, ":", end = " ")
    y = eval(input(" Please enter an integer between 1 and 10: "))
    if y == x:
      print("You got it!")
      break
    if j == 2:
      print("Too bad.  The number is: ", x)
      break
    if y < x:
      print("Your guess is too small.")
    else:
      print("Your guess it too big.")
  
guess()