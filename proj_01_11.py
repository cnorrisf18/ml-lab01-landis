

import requests
from bs4 import BeautifulSoup
import time
import re

def read_fileAsList( fname ):
    with  open(fname) as f:
        return [  (line[:-1] if line[-1] == "\n" else line) for line in f.readlines()]


def find_lineWithTextInList(direction, somelist,  sometext, startingPoint = None):
    if (startingPoint is None):
        i = len(somelist) // 2
    else:
        i = startingPoint
    while (i >= 0 and i < len(somelist)):
        if sometext is "" and somelist[i].strip() == "":
            # we have found a blank line, which is what we were looking for.
            return i
        elif sometext.lower() in somelist[i].lower():
            # we found the marker text.
            return i
        i = i + direction
    return False


def extract_GutenText(lines):
    startpoint1 = find_lineWithTextInList(-1, lines, "project gutenberg")
    startpoint2 = find_lineWithTextInList(1, lines, "", startpoint1)
    endpoint1 = find_lineWithTextInList(1, lines, "project gutenberg")
    endpoint2 = find_lineWithTextInList(-1, lines, "", endpoint1)
    return lines[startpoint2+1: endpoint2]



def get_gutentextURLs() :
    # find a random set of gutenberg texts in english
    # And parse it into beautiful soup!
    startURL = 'https://www.gutenberg.org/ebooks/search/?sort_order=random&query=l.en'
    r = requests.get(startURL)
    soup = BeautifulSoup(r.text, "html.parser")
    # find all the links in the gutenberg query.
    links = soup.find_all("a", class_="link")
    # Go through and build a list of the book numbers out of the matching links.
    booknums = []
    for link in links:
        regex = r".*/(\d+)"
        test_str = link.get('href')
        matches = re.match(regex, test_str, re.IGNORECASE)
        if matches:
            #print(f"Matched: {matches[1]} - {test_str}")
            booknums.append(matches[1])
        else:
            #print("no match: ", test_str)
            pass

    baseURL = "https://www.gutenberg.org/ebooks/NNN.txt.utf-8"
    urls = [baseURL.replace('NNN', x) for x in booknums]
    return urls


def get_gutenTexts(numTexts = 2):
    # this with statement opens a large session
    # for making multiple requests. More efficient.
    urls = get_gutentextURLs()
    texts = []
    with requests.Session() as rsession:
        for url in urls:
            time.sleep(3)
            print(url)
            getresult = rsession.get(url)
            ## Insert code to split lines from the lab here.
            # remember the text of the result is getresult.text
            lines = getresult.text.splitlines() #  ????
            gutenText = extract_GutenText((lines))
            texts.append(gutenText)
            # quit once we exceed the allowed number of texts
            numTexts -= 1
            if numTexts == 0: return texts

    return texts


class MarkovModel:
    def __init__(self, depth=2):
        self._prefix = tuple('' for i in range(depth))
        self.depth = depth
        self.model = {}

    def addWord(self, word):
        word = word.strip()
        prefix = self._prefix
        # find the prefix in the model or get an empty word count cause it's not there.
        countsDictionary = self.model.get(prefix, {})
        # Add 1 to the word count if it's there or store it as 1.
        countsDictionary[word] = countsDictionary.get(word, 0) + 1
        # save the word count back into the model.
        self.model[prefix] = countsDictionary

        # update the prefix
        self._prefix = self._prefix[1:] + (word,)

        print(f"Added '{word}' to model: {self}")

    def __str__(self):
        return f"Markov Model depth {self.depth} # keys {len(self.model)} prefix is {self._prefix}"



def test_MarkovModel():
    m = MarkovModel()
    words = '  what a day a dad had - a dad had a day - a dad day day '.split()
    for word in words:
        m.addWord(word)
    assert m.model[('a','dad')]['had'] == 2, "We didn't build it right for a dad."
    assert m.model[('a','day')]['-'] == 1, "We didn't build it right for a day."


if __name__ == '__main__':
    #texts = get_gutenTexts()
    m2 = MarkovModel()
    m4 = MarkovModel(4)
    m2.addWord("  fred  ")
    str(m2)


