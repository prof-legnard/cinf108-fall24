# Lab 2: Guess the number
Write a program that let's the user running it play a game where they have to guess a number between 1 and 25.
The player gets 5 guesses to guess the number, and potentially 6 if they guess close to the chosen number.

Don't forget to use the [template code](https://github.com/prof-legnard/cinf108-fall24/blob/main/lab2/lab2_template.py)

## Rules:
- Name your `.py` file according to the usual expected convention: `lastName_firstName_lab2.py`
- The player should be able to run the game within the terminal or command prompt with either:
       `python LastName_FirstName_lab2.py`  or `python3 LastName_FirstName_lab2.py`
- The player starts with 5 guesses.
- when the player is within 3 of the correct number, their max guess count increases by 1 
  (ex. correct number is 20, player guesses a number between 17-23, but doesn't guess 20, they get an extra guess)
- when the players gets an extra guess, they don't get any more extra guesses for the rest of the game.
  (ex. correct number is 20, players previously guessed 17, guesses 18, doesn't get any more bonus guesses, the `guess_count` increments as it normally would )
- Every prompt to guess must show remaining guesses OR show what guess out of MAX GUESSES they are at (be mindful of the bonus guess)
- A guess doesn't count if it's not between 1 and 25, the `guess_count` doesn't change, the user must guess again. ( `< 1` doesn't count, ` > 25` doesn't count)
- When the player guesses the correct number, they win and the program exits the game.
- When the player runs out of guesses, they lose and the program exits the game.

## Add print statements to indicate when the following conditions are met:
- The player is prompted to guess a number in the given range
- The player guesses the number, and wins (the program should then finish)
- The player runs out of guesses and loses
- The player is within +/- 3 of the correct number, and gets an extra guess
- The player is within +/- 3 of the correct number, but doesn't get any more guesses
- The game scolds the user if a number is greater than 25 or less than 1, does not use a guess

## Requirements for credit **(25 points)**:
- Use conditional statements (at least one of if, elif, else), logical operators (at least one of >, <, ==, or, and etc..) 
    with a loop to create the game **(10 points)**. A while loop has been provided in the template, but you may use a for loop 
    to manage your program's game cycle. (10 points).
- Define and call at least one function of your creation **(3 points)**
- messages included for all conditions that need to be met **(6 points)**
- no errors, code executes game correctly following all rules. **(6 points)**

## Tips and hints for writing this program
1. Run the sample code, what does it currently do?
2. Copy the sample code to your own `.py` file. Update the sample code to guess if the guessed number is equal to the winning number.
   - If it does, print a message signaling they won and exit the loop, then exit the program.
   - Else, prompt the user they guessed wrong and to guess again, increment `guess_count`
   - If `guess_count` == `max_guesses`, the current loop will exit, it means the player has run out of guesses and they lost. How can you then provide a message to the user that they lose
4. once this is working, what other conditions need to be met? what other conditional statements can we use to test them? Refer to the lecture notes on conditional statements.
5. If you're not sure how to start, or what to do next. Reread the rules, break the problem into smaller chunks. Which of the above conditions can you meet, while ignoring the others?
6. If you're still stuck: **Reach out to the instructor and ask for help.** You have resources such as Brightspace, Slack, and Email at your disposal.

## Example Output for the game:

### The player loses
```
Guess the number between 1 and 25. You have 5 guesses.
Guess # 1, 5 remaining 
[enter a # from 1-25]: 3
Guess incorrect, guess again.
Guess # 2, 4 remaining 
[enter a # from 1-25]: 18
Guess incorrect, guess again.
Guess # 3, 3 remaining 
[enter a # from 1-25]: 19
Guess incorrect, guess again.
Guess # 4, 2 remaining 
[enter a # from 1-25]: 12
You are close, +1 guess, you now have 2 remaining.
Guess # 5, 2 remaining 
[enter a # from 1-25]: 13
You are close, you now have 1 remaining.
Guess # 6, 1 remaining 
[enter a # from 1-25]: 14
Guess incorrect, guess again.
The correct number was 10. You lose.
```

### The player wins:
```
Guess the number between 1 and 25. You have 5 guesses.
Guess # 1, 5 remaining 
[enter a # from 1-25]: 14
You are close, +1 guess, you now have 5 remaining.
Guess # 2, 5 remaining 
[enter a # from 1-25]: 15
Guess incorrect, guess again.
Guess # 3, 4 remaining 
[enter a # from 1-25]: 13
You are close, you now have 3 remaining.
Guess # 4, 3 remaining 
[enter a # from 1-25]: 12
You are close, you now have 2 remaining.
Guess # 5, 2 remaining 
[enter a # from 1-25]: 11
You guessed the correct number 11, you win!
```
