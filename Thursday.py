"""
Copy paste these instructions in there.  (copy out everything highlighted)
Look through the "links" variable and see if you can find some image covers.
Edit Proj_01_08 to make the loop in proj_01_08 print out the path to the images for all of the book cover thumb images.
"""
import requests
from bs4 import BeautifulSoup
import re
startURL = 'https://www.gutenberg.org/ebooks/search/?sort_order=random&query=l.en'
r = requests.get(startURL)
soup = BeautifulSoup(r.text, "html.parser")
# find all the links in the gutenberg query.
links = soup.find_all("img")
# Go through and build a list of the book numbers out of the matching links.
booknums = []
for link in links:
    regex = r".*epub.(\d+).*"
    test_str = link.get('src')
    try:
        matches = re.match(regex, test_str, re.IGNORECASE)
    except:
        matches = False
        print("FAILURE",link,"does not have an image file")
        pass
    if matches:
        print(f"Matched: {matches[1]} - {test_str}")
        booknums.append(matches[1])
    else:
        print("no match: ", test_str)


"""
After part 1 make a new multiline comment for this part and copy the instructions and paste into Thursday after this part.
Let's suppose we want to track wins at pingpong by the 6 members of our class:  Chloe, James, Lesley, Hannah, Sierra, Mars
In your code, make a dictionary called pingpongwins that stores 5 wins for Chloe, 3 for James, 5 for Lesley, 2 for Hannah, 3 for Sierra, and 0 for Mars (who is very bad at ping pong).  You can make up your own numbers.  But make sure at least two players tie for the top number of wins.
Test your code by printing the wins for Sierra, using the dictionary "get" method.
Test your code on a nonexistent team member using "get" method on a dictionary to get the number of wins for "Bob".
Write a statement to print the total number of games played, using the python sum function, and the values() method on a dictionary
Write a for loop to use the items() method on a dictionary to print out a table that looks like this:
    Winners of PingPong
Chloe        5 wins
James        3 wins
Lesley        5 wins
etc.
Order may be different!

Challenge: Write a conditional list comprehension to derive a list of all of the people that have won the maximum number of games.  Use the max builtin function, the keys.  You'll need the items() method on a dictionary to step through all the key value pairs.  You'll need the max builtin function.  You'll need the values() method. 
"""

