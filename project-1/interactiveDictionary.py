#Interactive Dictionary
import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    errorStatement = "Error: Word does not exist"
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? (y/n): " %get_close_matches(w, data.keys())[0])
        if yn == "y" or yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n" or yn == "N":
            return errorStatement
        else:
            return "We did not understand your query"
    else:
        return errorStatement

word = input("Please enter a word: ")
output = translate(word)

if type(output) == list:
    for i in range(len(output)):
        print(str(i+1)+')', output[i])
else: 
    print(output) #will always return a single string otherwise (aka only for error statement)
