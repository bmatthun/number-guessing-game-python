import art
import random

MIN_NUM = 1
max_num = 100
EASY_MODE_ATTEMPTS = 10
HARD_MODE_ATTEMPTS = 5

print(art.logo)
print('''
Welcome to the Number Guessing Game!
You'll have to guess the right number between 1 and another number that you choose!
If you don't choose anything the default number is 100.''')

while True:
    chosen_number = input(f"Please type an arbitrary number above 1 or just hit Enter:\n")
    if not chosen_number.isdigit():
        print("Not valid input!")
    elif chosen_number == "":
        break
    else:
        max_num = int(chosen_number)
        break

level_selection = input("Please choose difficulty: 'easy' or 'hard'?\n")

def game(maximum_number, attempts):
    random_number = random.randint(1, maximum_number)
    while attempts > 0:
        print(f"You have {attempts} left")
        guess = input("Take a guess!\n")
        if not guess.isdigit():
            print("Not a valid input!")
            continue
        if int(guess) == random_number:
            print("Wow! You guessed it! You won! :D")
            break
        elif int(guess) > random_number:
            print("Number too high! Try again!")
            attempts -= 1
        else:
            print("Number too low! Try again!")
            attempts -= 1
    if attempts == 0:
        print(f"Out of attempts, you lost... :// The number was: {random_number}")

while True:
    if level_selection == "easy":
        game(max_num, EASY_MODE_ATTEMPTS)
        continue_game = input("Would you like to play again? [y, n]")
        if continue_game == "y":
            chosen_number = input(f"Please type an arbitrary number above 1 or just hit Enter:\n ")
            if chosen_number != "" and type(int(chosen_number)) == "int" and chosen_number > 1:
                max_num = int(chosen_number)
            level_selection = input("Please choose difficulty: 'easy' or 'hard'?\n")
            continue
        break
    elif level_selection == "hard":
        game(max_num, HARD_MODE_ATTEMPTS)
        continue_game = input("Would you like to play again? [y, n]")
        if continue_game == "y":
            chosen_number = input(f"Please type an arbitrary number above 1 or just hit Enter:\n ")
            if chosen_number != "" and type(int(chosen_number)) == "int" and chosen_number > 1:
                max_num = int(chosen_number)
            level_selection = input("Please choose difficulty: 'easy' or 'hard'?\n")
            continue
        break
    else:
        print("Again...")
