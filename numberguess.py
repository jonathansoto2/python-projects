'''
Jonathan Soto

generate a RANDOM NUMBER 1-100 
user will input a guess
will output if either too high or too low
guess correctly will say congrats and ask to play again
keep count of how many guesses
'''
import random

guess = []
r = random.randint(1,101)
play = 'y'

def check(x):
  
  if x == r:
    display = 'Congratulations you\'ve won! You guessed {} times.'.format(len(guess))
    print(display)
    play = input('Would you like to continue playing? (y/n) ')

  if x > r:
    print('It looks like you have guessed a little too high. Try again.\n')
    guess.append('high')
  elif x < r:
    print('It looks like you have guessed a little too low. Try again.\n')
    guess.append('low')

def main():
  print('\nTry and guess the randomly generated number!')
  g = int(input('Enter your guess: '))
  check(g)

if __name__=='__main__':
  while play == 'y':
    main()