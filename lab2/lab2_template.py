"""
Lab 2: Guess the number
Write a program that let's the user running it play a game where they have to guess a number between 1 and 25
The player gets 5 guesses to guess the number, and potentially 6 if they guess close to the chosen number.

Rules:
- Name your `.py` file according to the usual expected convention: `lastName_firstName_lab2.py`
- The player should be able to run the game within the terminal or command prompt with either:
       `python LastName_FirstName_lab2.py`  or `python3 LastName_FirstName_lab2.py`
- when the player is within 3 of the correct number, their max guess count increases by 1 
  (ex. correct number is 20, player guesses a number between 17-23, but doesn't guess 20, they get an extra guess)
- when the players gets an extra guess, they don't get any more extra guesses for the rest of the game.
  (ex. correct number is 20, players previously guessed 17, guesses 18, doesn't get any more bonus guesses, the `guess_count` 
  increments as it normally would )
- Every prompt to guess must show remaining guesses OR show what guess out of MAX GUESSES they are at (be mindful of the bonus guess)
- A guess doesn't count if it's not between 1 and 25, the `guess_count` doesn't change, the user must guess again. 
  ( `< 1` doesn't count, ` > 25` doesn't count)
- When the player guesses the correct number, they win and the program exits the game.
- When the player runs out of guesses, they lose and the program exits the game.

Add print statements to indicate when the following conditions are met:
- The player is prompted to guess a number in the given range
- The player guesses the number, and wins (the program should then finish)
- The player runs out of guesses and loses
- The player is within +/- 3 of the correct number, and gets an extra guess
- The player is within +/- 3 of the correct number, but doesn't get any more guesses
- The game scolds the user if a number is greater than 25 or less than 1, does not use a guess

Requirements for credit (25 points):
- Use conditional statements (at least one of if, elif, else), logical operators (at least one of >, <, ==, or, and etc..) 
    with a loop to create the game (10 points). A while loop has been provided in the template, but you may use a for loop 
    to manage your program's game cycle. (10 points).
- Define and call at least one function of your creation (3 points)
- messages included for all conditions that need to be met (6 points)
- no errors, code executes game correctly following all rules. (6 points)

"""
import random

# using global variables
MIN = 1
MAX = 25
win_num = random.choice(range(MIN, MAX))

guess_count = 1
max_guesses = 5
bonus = False
you_win = False

print(f"Guess the number between {MIN} and {MAX}. You have {max_guesses} guesses.")
while guess_count <= max_guesses:
    # your main game loop code should go here.
    guess = input(
            f"[enter a # from {MIN}-{MAX}]: "
        )
    print(f"This is a demo print statement for showing how while loops work. Remove this line or modify it for your submission. \n \
           Your current guess is {guess}. You are  on guess # {guess_count} of {max_guesses}"
    )
    # don't forget to increment your guess_count so the loop exits properly.
    # you may need to modify this or add other increments or decrements based on your game logic design.
    guess_count += 1

if True:
    # modify your if statement and have it do "something" in the scope below
    # Don't forget to indent your code properly.
    print("This if statement is true. Did the player win or lose?")

if you_win == True:
    print("This if statement is false. Does this even print?")
