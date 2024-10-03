# Lab 4

For this Python Exercise, you will work with an already written Python script and add some additional functionality. In `lab4_template.py` I have a written python script that will read in the contents of `song_list.txt`, select 12 songs, and add them to a new file called `setlist.txt`

Read from a list of songs called "song_list.txt". Work with an already existing code base and add some improvements. Write the setlist to a file called `setlist.txt`. Each song should be on it's own line with the number associated with it starting at 1. You have the set `selected_songs` already provided for you in the lab template code if you start from that point.

Start by making a folder for lab4 on your computer, and placing both files in that folder. Open VSCode and start a workspace in this same folder. You will want both your `.py` file and the input file `song_list.txt` to be located in this folder, and have VSCode running your script from this directory as well.

Complete the following exercises in Python to include in your submissio `.py`. Try to structure your code according to the PEP-8 standard. You should run `lab4_tempate.py` to make sure to start you can print out 12 songs (this part is already written.) Then save a copy of this template with the normal convention of `lastname_firstname_lab4.py1`. Write additional code in your submission file to solve the following:

1. Add a line indicating a set break halfway through the set (what index would be applied). A set break can be indicated by text such as SET BREAK or lines or characters splitting the first half of the set list from the second
i.e. ####, ------, %%%%%.  See `demo_setlist.txt` for example output.
1.  Sometimes the band will be brought on for an encore, write and call a function to read in setlist.txt, and
append two songs from `song_list.txt` to  another file called "setlist_with_encore.txt"
to the end of the setlist.txt. Indicate either on those lines or before they are listed that they are part of the encore
1. write a function that checks how many songs (lines) are in a file, it should be able to take `song_list.txt`, setlist.txt, 
or any .txt file as an input. It should not cound any set break or encore lines (maybe mark those lines with a character like "--" 
to identify and filter out
1. add some code (maybe write and call another function?) to read through song_list.txt, identify any songs that contain the word "and".
save the "and" songs to a variable (list/tuple/set/dictionary), Call your function with "song_list.txt" as an input and Write that data structure to a file called and.txt

Your .py file should be able to take in `song_list.txt` and generate all the output files mentioned in the instruction to receive full credit.
You do not need to submit your final .txt files, just make sure when I run your code the files will be created and have the
correct data written to them.

Your final script should take in `song_list.txt` and work with the list of songs in the file to spit out new lists saved in the following files. **You only need to submit your `.py` file on Brightspace.** When I run your code it should create two files with these names:

```
setlist.txt
and.txt
```
