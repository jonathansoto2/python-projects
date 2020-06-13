# In-Class Assignment 2
# Powerball
# Boston Cartwright, Dallin Kimber, and Jonathan Soto

'''
Write a program in Python that asks the user if he or she would like to play Powerball. 
If the answer is yes, ask the user to enter his or her first, middle, and last names. 
Generate five random numbers from 1 to 69 and one random number from 1 to 26. Of the
 first five random numbers, no two can have the same value. Present the information as:
  last name, first name and middle name The Winning Powerball Numbers Are: XX XX XX XX XX   XX

A function will be called from main with the six numbers being sent to the function as
 its argument, and the function will return the sum of the six numbers, and the sum 
 will printed in main with the appropriate message.

The user will be given the option to play again, otherwise go to end of job.

The program should be very user friendly and the code should be well documented.
 Be very thorough with your edit checks.
'''

import random

# main entrance of program


def main():
    print("Welcome to Powerball!")

    # ask the user if they want to play
    ask_to_play()

    

def play():
    # names will be a tuple of three strings
    names = ask_for_names()

    # numbers will be a tuple of six integers
    numbers = generate_numbers()

    # prints the winning numbers
    print_numbers(names, numbers)

    # ask to play again
    ask_to_play()


def ask_to_play():
    response = str(input("Would you like to play? (Enter Y/N): "))
    if response not in ['y', 'Y', 'n', 'N']:
        print("Please enter either a 'Y' or an 'N' as a response.")
        ask_to_play()
    elif response in ['N', 'n']:
        print("Please play again!")
        quit()
    play()


# ask for names
def ask_for_names():
    first_name = input("What is your first name?: ")
    middle_name = input("What is your middle name?: ")
    last_name = input("What is your last name?: ")

    if len(first_name) > 25 or len(middle_name) > 25 or len(last_name) > 25:
        return ask_for_names()

    return {
        'first': first_name,
        'middle': middle_name,
        'last': last_name
    }

# generate powerball numbers


def generate_numbers():
    numbers = []

    # generate first five numbers (1-68)
    for _ in range(5):
        number = random.randint(1, 69)
        while True:
            try:
                numbers.index(number)  # see if number exists
                number = random.randint(1, 69)
            except ValueError:  # if number does not exist, we are good
                break
        numbers.append(number)

    # generate last number (1-26)
    numbers.append(random.randint(1, 26))

    return numbers


# print winning numbers
def print_numbers(name, numbers):                                
    print(str.format("Thank you for playing powerball {} {} {}. \n The Winning Numbers are {:02} {:02} {:02} {:02} {:02} {:02}.",
                     name['first'], name['middle'], name['last'], numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5]))


main()
