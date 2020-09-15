
from random import *
guessesTaken = 0
print('What is your name?')
myName = input()
number = randint(1, 5)
print('Hello, ' + myName + ', I am thinking of a number between 1 and 5')
while guessesTaken < 4:
  print('Take a guess')
  guess = int(input())
  guessesTaken = guessesTaken + 1
  print('Guess is too low. Try again')
  if guess > number:
    print('Guess is too high. Try again')
  if guess == number:
    break


if guess == number:
  guessesTaken = str(guessesTaken)
  print('Good job, ' + myName + '! You guessed the correct number in ' + guessesTaken + ' guesses!')

#e
if guess != number:
  number = str(number)
  print('oops. You have reached the guessing limit. The number that I was thinking is ' + number)
