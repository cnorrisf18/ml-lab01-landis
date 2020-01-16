
"""
Lab 01 - Project 01 - Re-acquainting with Python

01-03 functionizing
"""

def double_letter_list(somestring):

    result = []
    for c in somestring:
        result.append(f"{c}---{c}")
    return result



"""
Note that you can select these lines too and "run selection in console.  One at a time.
"""
double_letter_list("123")
double_letter_list("abcdef")
mylist = double_letter_list("12")

double_letter_list(mylist)  # whoa.  Dude.



# You can do the above as a list comprehension...  The above function could be replaced with this:
#
#     return [ f"{c}---{c}" for c in somestring ]
#


# Write a function that takes one parameter - the name of a file to read -
# Do a google search for "how to read a file without newlines" ...
#  And return a list of lines without the newline character.
# It may be best to make a note of the fact the last line of the file
# may or may not have a new line on the end of it.
#
# Your function should be called read_fileAsList

def read_fileAsList( fname ):
    # Your code here:
    file = open(fname, "r")
    line_list = []
    for line in file:
        line = line.rstrip("\n")
        line_list.append(line)
    return line_list

"""

01-04 making it good... using "with"

"""

# 01.04 - It's better to use a "with" statement to open a file.
#
#  Rewrite the above function using a "with" statement.
# Note: It is not an error to redeclare the function... it will overwrite the first one.

def read_fileAsList( fname ):
    # Your code here:
    with open(fname, "r") as file:
        line_list = []
        for line in file:
            line_list.append(line.rstrip("\n"))
    return line_list










