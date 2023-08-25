from game_data import data
from os import system, name
import art
import random

# Clear screen function


def clear():
    """ Clear terminal function """

    # This is for Windows
    if name == 'nt':
        _ = system('cls')

    # This is for Mac, Linux
    else:
        _ = system('clear')


def game_start():
    """ Starts Higher/Lower game """

    score = 0
    keep_playing = True

    # assign entry_a to a random data point outside of loop
    entry_a = random.choice(data)

    while keep_playing != False:

        # Assign entry_b to a random data point INSIDE of loop (this is important)
        entry_b = random.choice(data)

        # If entries are identical then entry_b will re-roll till they are no longer the same
        while entry_a == entry_b:
            entry_b = random.choice(data)

        higher_entry = {}
        if entry_a.get('follower_count') > entry_b.get('follower_count'):
            higher_entry = entry_a
        else:
            higher_entry = entry_b

        # Ask user who they believe has more followers

        print(
            f"Compare A: {entry_a.get('name')}, a {entry_a.get('description')}, from {entry_a.get('country')}")
        print(art.vs)
        print(
            f"Against B: {entry_b.get('name')}, a {entry_b.get('description')}, from {entry_b.get('country')}")

        answer = input("Who has more followers? Type 'A' or 'B': ")

        # Assign user answer to corresponding entry
        if answer == 'A':
            answer = entry_a
        elif answer == 'B':
            answer = entry_b
        else:
            print("You have provided an invalid answer choice")

        # If user is correct continue game and iterate score, otherwise end game and display score
        # Compare answer given to entry data
        if answer == higher_entry:
            score += 1
            clear()
            print(art.logo)
            print(f"You're right! Current score: {score}")

            # Assign answer to entry_a to keep streak going
            entry_a = answer
        else:
            clear()
            print(f"Sorry, that's wrong. Final score: {score}")
            keep_playing = False


print(art.logo)
game_start()
