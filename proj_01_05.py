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
def find_lineWithTextInList(direction, somelist,  sometext, startingPoint = 0):
    try:
        while 0 < startingPoint < len(somelist):
            if sometext.lower() in somelist[startingPoint].lower():
                print("text found on line",startingPoint)
                break
            startingPoint += direction
        while 0 < startingPoint < len(somelist):
            if somelist[startingPoint].strip() == "":
                print("blank text found on line",startingPoint)
                return startingPoint
            startingPoint -= direction
    except IndexError as e:
        print("index error")
        startingPoint = 0
    print("starting point is",startingPoint)
    return False





# 01.05 - do this before 01.06.
def extract_GutenText(lines):
    # Look for "project gutenberg" before the mid point
    # I am including some sample code to get you started.....
    # Make sure you understand what this does BEFORE you copy it and modify it for below.
    # Also it's incomplete....
    startpoint1 = (len(lines) // 2)- 1   # note the integer division.
    startGut = find_lineWithTextInList(-1, lines, "project gutenberg", startpoint1)
    endGut = find_lineWithTextInList(1, lines, "project gutenberg", startpoint1)
    # try:
    #     while startpoint1 > 0:
    #         if "project gutenberg" in lines[startpoint1].lower():
    #             #we have found the point where the header ends
    #             print("Project gutenberg found on line", startpoint1)
    #             break
    #         startpoint1 = startpoint1 - 1 # or alternatively:  startpoint1 -= 1
    # except IndexError as e:
    #     # we had a an index out of bounds problem in the above code.
    #     print("Error error - bounds error in finding start point!")  # in general it's not a good idea to print in your exceptions.
    #     startpoint1 = 0
    #
    # # look for the first blank line after that point.
    # while startpoint1 < len(lines):
    #     if lines[startpoint1].strip() == "":
    #         print("Header should start at ", startpoint1)
    #         break
    #     startpoint1 = startpoint1 + 1
    #
    # # look for "project gutenberg" after the midpoint
    # startpoint2 = len(lines) // 2
    # try:
    #     while startpoint2 < len(lines):
    #         if "project gutenberg" in lines[startpoint2].lower():
    #             #we have found the point where the footer begins
    #             print("Project gutenberg found on line", startpoint2)
    #             break
    #         startpoint2 = startpoint2 + 1
    # except IndexError as e:
    #     print("Bounds error in finding finish point!")
    #     startpoint2 = len(lines)
    #
    # # look for the first blank line before that point
    # while startpoint2 > 0:
    #     if lines[startpoint2].strip() == "":
    #         print("Footer should start at ", startpoint2)
    #         break
    #     startpoint2 = startpoint2-1
    #
    # result = lines[startpoint1 +1:startpoint2]
    print(startGut,endGut)
    if endGut is False and startGut is not False:
        result = lines[startGut+1:]
    else:
        result = lines[startGut+1:endGut]
    print(result)
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



@raises(ValueError)
def test_totally_empty_GutenText():
    text=""
    lines=extract_GutenText(text)



@raises(ValueError)
def test_multiple_GutenTexts():
    text="""Project Gutenberg
    Project Gutenberg
    Project Gutenberg
    Project Gutenberg
    Project Gutenberg
    Project Gutenberg
    Project Gutenberg
    Project Gutenberg
    Project Gutenberg
    """.split("\n")
    print(text, len(text))
    lines = extract_GutenText(text)
    assert len(lines) == 0, "there is no start or finish to this text, so there should be an empty result"


def test_only_one_GutenText():
    text="""This is a test example
    *** Project GUTENberg should start here after the blank line ***
    *** and not include this line or the blank line after this one **
    
    guten text is here!
    
    ** some nonlank line **
    *** text should end here but the blank line before it should also not be included ***
    ** none of this should show up
    """.split("\n")
    lines = extract_GutenText(text)
    assert lines[0] == "    guten text is here!", "there is no end point so just go after the start"
    assert len(lines) == len(text) - 4 , f"{len(text)-4} should be the length of text but {len(lines)} is the length of the text!"