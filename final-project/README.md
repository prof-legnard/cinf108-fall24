# The Final Project

Your final task for the course will be to create a TODO List command line interface (CLI) tool in Python. The CLI tool will allow you to create, change completion status, and edit items written out in a "TODO list".

You will be utilizing all of the skill and your knowledge of Python you have acquired so far in the course to create this CLI.

You should be able to interact with this TODO list utility from the command line. I will leave it up to you if you'd like to use `sys.argv`, `argparse`, or a combination of the two. Using `argparse` will require more code but will allow for more flexible usage of your tool.

## Functionality Requirements
1. By default, your CLI tool should write to a file called `TODO.txt`, `TODO.csv`, or `TODO.json`. (You may use the output format of your choice)
2. You should be able to have a subcommand, either by positional argument or a flag that will display your current TODO list items by reading them from your `TODO` save file.
3. Each TODO list item should have: 
   - an `id` value
   -  ad `topic` or `category` of the type of task (think of how you would categorize your assignments due for various classes) 
   -  a `description` of what the task is doing, 
   -  status of the TODO item (incomplete/in progress/complete)
4. With defined input arguments,your TODO list CLI tool should be able to modify your final TODO list file:
   - add new items to your TODO list file
   - change the status of the TODO item (incomplete/in progress/complete)
   - update previously added TODO items (description, date, category, etc.)
5. Add an option to be able to create or update a *separate* TODO list file with a different name (TODO2.txt, work-todo.csv, chores.csv, etc...)
    - your CLI tool can write to a file like `TODO.txt` by default, but you should be able to manage multiple todo lists with a separate argument.

    For example by passing a `--list-name` argument you can point to a new or already defined `TODO` list file so that the tool can manage multiple lists.

### Clean Code Requirements
1. Use `Error` statements of various types and `print()` statements to provide proper feedback to the users. 
2. Apply sufficient comments to your code explaining how it works.
3. Name your submission `.py` file `lastname_firstname_todo.py`. For your submission, post your final .py file on your github and send me the link in the Brightspace Submission.

### BONUS (10 points)
Write a class or multiple classes to manage TODO items. Implement methods and attributes to manage writing to your TODO list files, displaying information about TODO items, etc.
Utilizing a class instance to add/change status/edit TODO list items loaded in from a file would be sufficient for getting full credit for the bonus. YOUR CODE MUST STILL WORK PROPERLY TO GET CREDIT FOR THE BONUS.

