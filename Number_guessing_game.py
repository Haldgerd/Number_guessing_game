from random import randint

import pyfiglet
from termcolor2 import c

# GLOBAL/FIXED VARIABLES
HARD_DIFFICULTY = 5
EASY_DIFFICULTY = 10

# try to figure out how to make size of terminal larger/wider so title can be expanded.
# MAIN CODE NEEDS SERIOUS REFACTORING!!!

# TITLE
ascii_title = pyfiglet.figlet_format("Guess the number", font="slant")
colored_title = c(ascii_title)
print(colored_title)
print("Welcome to the Number guessing game!")
print("I'm thinking of a number between 1 and 100. Which number did I choose?\n")
# FUNCTIONS


def select_random_number():
    """
    Returns a randomly chosen number.
    :return: integer number
    """
    random_number = randint(1, 100)
    return random_number


def difficulty_selection():
    """
    Returns life pool (lives) determined in correspondence to difficulty chosen by the user.
    :return: integer number representing max life.
    """
    difficulty = input("Please choose your difficulty level. Type 'easy' or 'hard':\n").lower().strip()
    if difficulty == "easy":
        return EASY_DIFFICULTY
    else:
        return HARD_DIFFICULTY


def guess_checker(random_number):
    """
    Return a answer to the user about their number guess. Determined by given conditions, an answer is returned
    informing the user about their guess.
    :param random_number: parameter which accepts an randomly chosen integer.
    :return: string. Answer to the user about their guess.
    """
    guess = int(input("Make a guess: "))

    if guess == random_number:
        return f"\nYou've guessed the number. It is indeed {random_number}! YOU WIN!"
    # elif (abs(guess) - abs(random_number)) <= 5:   # <<< PRODUCING A BUG!
    #    return "Very close."
    elif guess < random_number:
        return "Too low."
    else:
        return "Too high."


# VARIABLES
game = True

# MAIN LOGIC
while game:
    number = select_random_number()
    print(number)
    life_count = difficulty_selection()
    print(f"You have {life_count} attempts to guess the number.")

    while life_count > 0:
        guess_result = guess_checker(number)
        print(guess_result)

        if guess_result in ["Too high.", "Too low.", "Very close."]:
            life_count -= 1
            if life_count == 0:
                break
            elif life_count == 1:
                print(f"You have 1 attempt left remaining.")
            else:
                print(f"You have {life_count} attempts left remaining.")
        else:
            break

    if life_count == 0:
        print("You ran out of attempts. YOU LOSE!")

    another_play = input("\nWould you like to play again? Type 'yes' to play again or 'no' to exit.").lower()
    if another_play in ["y", "yes"]:
        continue
    else:
        game = False

print("Goodbye!")
