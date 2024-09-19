# Lab 3
For this lab we are going to work with dictionaries to analyze some historical U.S. stock market data. This will test your ability to work with dictionaries and lists (or tuples). You may use your full knowledge of Python to solve each question. Remember that you have the following at your disposal:
- loops (for/while)
- conditional statements (if/elif/else)
- functions (create your own `def`, use built-ins)
- lists, dictionaries, tuples, strings (any standard data types we have gone over)
- list comprehensions

You may not import any external public Python libraries for this assignment. I want to see you work with the tools above.

Starting with the lab3 files, `lab3_template.py` and `stock_data.py`, run `lab3_template.py` to familiarize yourself with a python dictionary, and accessing it's keys and values. Then add code to answer the questions below.  Submit one `.py` file with the answers to the questions. You do not need to submit `stock_data.py` Make sure the import statement at the top of the template code is in your submission, and you are using `STOCK_DATA` in some capacity, or else when I run your code to grade it won't work, and you will lose points.

## Setup Instructions
Create a `lab3` folder on your computer. Download the contents of the `lab3` folder in this github repository into your `lab3` folder. 

(you can either the code and save it into a file, hit the download button in the Github UI,  or if you have working knowledge of `git`, and can figure it out, clone it to your desktop)  

Before you start, your folder should contain the following:
```
├── README.md
├── lab3_template.py
└── stock_data.py
```
You will need `stock_data.py` for `lab3_template.py` to work. **Do not modify** `stock_data.py`. 

Open a VSCode workspace from this folder (or set the current working directory or Powershell/terminal to be this folder). Run `lab3_template.py`
Once you are able to run `lab3_template.py`, save it as your lab submission file: `lastname_firstname_lab3.py`.

You may modify the template code as you see fit, just do not modify `stock_data.py`, or modify the `import` statement on line 1 of `lab3_template.py`. You may work with the global `STOCK_DATA` variable as is, but I have provided some code that converts it into a nested dictionary, if that's easier for you to use.
After completing the following, and checking to make sure your code runs, submit your `lastname_firstname_lab3.py` file on Brightspace.

## Stock Analysis Questions

You can now answer the questions below, and attach this `lastname_firstname_lab3.py` file in your submission. **For any calculations with prices, round to two decimal places, and include dollar signs**. Each question is worth up to 5 points.

1. **Print the difference between the final 2007 price of each stock and the 2002 price.** Use conditional logic to indicate with a print statement whether the stock price went up or down. Make sure to include the name or symbol of the stock with each price difference i.e.:
```
3M price difference: $51.57. The price went up!
Amazon price difference: $76.42. The price went up!
Ford price difference: $-1.26. The price went down.
```
2. **What is the average initial price of all of the companies?** Calculate using what you know in Python. Use a print statement and label it so it's seen in the output of your script: "The average initial price is ..."

3. Save all the stock tickers (The 3-5 letters labeled with "symbol".) to a data structure, you may choose the type (list, dictionary, tuple, string), sort the values to be in alphabetical order using Python. **Print all of the tickers in a loop, in alphabetical order, two tickers per line.**
```
AMZN CPB
DIS DOW
F GIS
# (and the tickers keep going downward)
```

4.  **Which company name (not symbol) had the highest stock price in 2002? Which company had the lowest?** Use python, via a combination of the `stock_dict` variable, loops, lists, dictionaries, or if/elif/else statements to calculate your answer. If writing a function helps you keep your code organized and easily repeatable, write and call that in your solution.  Show your work, label your answer in a print statement, i.e. "The stock with the lowest price in 2002 was {company name}"
HINT: A list of dictionaries, a list of tuples, or a list of list, or other nested data structures may be helpful. Also, what's the built-in python function to sort things?

5. **Which stock had the lowest stock increase (decreases in price do not count!) from their initial price to 2007?** Don't just print the difference and find the highest increase by looking, use Python to track it. You may have to create a variable to set the current highest price found, and update that value if a higher one is found. Or make another list of dictionaries/lists/tuples to help. With python code, identify and provide the stock symbol or company name with your answer in a print statement.


#### source links for Lab3:
https://gist.github.com/tanveery/4ac939d2ad27954da4c8db13e10ef7bd
