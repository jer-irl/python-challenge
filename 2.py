import requests
import copy

response = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")

with open('text', 'r') as file:
    text = file.read()


def findRareChar(text):
    dict = {}
    for char in list(text):
        if char in dict:
            dict[char] += 1
        elif char not in dict:
            dict[char] = 1
    itdict = copy.copy(dict)
    for key in itdict:
        if dict[key] > 1:
            del dict[key]
    return dict.keys()


def filterSource(text, rareChars):
    textlist = list(text)
    itlist = copy.copy(textlist)
    for char in itlist:
        if char not in rareChars:
            textlist.remove(char)
    return ''.join(textlist)

rareChars = findRareChar(text)
filtered = filterSource(text, rareChars)
print(rareChars)
print(filtered)
