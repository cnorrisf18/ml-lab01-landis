"""
Lab 01  Project 01-04.  extract_gutenText

Write the function extract_gutenText here and let's test it out!

So we'll also be writing a test function for this one.
"""

#  Copy and paste your code here from previous exercise:

def read_fileAsList( fname ):
    with  open(fname) as f:
        return [  (line[:-1] if line[-1] == "\n" else line) for line in f.readlines()]

# optional 01.06.  You can come back and do this LATER.
def find_lineWithTextInList(direction, somelist,  sometext, startingPoint = None):
    pass


# 01.05 - do this before 01.06.
def extract_GutenText(lines):
    # Look for "project gutenberg" before the mid point
    # I am including some sample code to get you started.....
    # Make sure you understand what this does BEFORE you copy it and modify it for below.
    # Also it's incomplete....
    startpoint1 = len(lines) // 2   # note the integer division.
    try:
        while """some condition here to prevent you from running off the beginning of the list """:
            if "project gutenberg" in lines[startpoint1].lower():
                break
            startpoint1 = startpoint1 - 1 # or alternatively:  startpoint1 -= 1
    except IndexError as e:
        # we had a an index out of bounds problem in the above code.
        print("Error error - bounds error in finding start point!")  # in general it's not a good idea to print in your exceptions.
        startpoint1 = 0

    # look for the first blank line after that point.

    # look for "project gutenberg" after the midpoint

    # look for the first blank line before that point


    result = a slice of the list that is just the text of the ebook.  Don't include the blank lines in the slice
    if len(result) == 0:
        raise ValueError("Book is empty.  May not have the right start and end markers.")
    return result



# Part 01.07 -
# Mars wrote this test FOR you.... pay particular attention to the notes in the lab
# and how it works!
# Especially string join, f-strings, assert.
#
# DO NOT GO ON if you don't understand how those work!
#


def test_basic_extract_GutenText():
    print("dude")
    texttext1 = """This is a test example
    *** Project GUTENberg should start here after the blank line ***
    *** and not include this line or the blank line after this one **
    
    guten text is here!
    
    ** some nonlank line **
    *** Project GutenBERG text should end here but the blank line before it should also not be included ***
    ** none of this should show up
    """
    testtextlines = texttext1.split("\n")
    actualtextlines = extract_GutenText(testtextlines)
    assert len(actualtextlines) == 1, f'Incorrect number of lines for testtext1: {len(actualtextlines)} should be 1. {"|".join(actualtextlines)}'
    assert actualtextlines[0] == "    guten text is here!", f"testtext1 is wrong: {'|'.join(actualtextlines)}"


"""
This SHOULD raise an exception - specifically a ValueError.
"""
from nose.tools import *
@raises(ValueError)
def test_empty_GutenText():
    text="""This text has
    no
    marker for start or end of book.
    """.split("\n")
    lines = extract_GutenText(text)  # This should throw an exception.  And Nose is expecting a "ValueError" exception.






