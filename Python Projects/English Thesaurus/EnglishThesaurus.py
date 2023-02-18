#loading json data
import json
#recommending the best match
from difflib import get_close_matches


data=json.load(open("data.json"))
#print(data)

#returning the defination of word

def translate(w):
    #implementing case sensitivity
    w=w.lower()
    if w in data:
        return data[w]
    #capital letters of first in word
    elif w.title() in data:
        return data[w.title()]
    #output for all caps
    elif w.upper() in data:
        return data[w.upper()]
    #recommending the best match
    elif len(get_close_matches(w,data.keys()))>0:
        #confirmation from the user input yn 
        yn = input("Did you mean %s isntead? Enter Y if yes, or N if no." % get_close_matches(w,data.keys())[0]) 
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    #taking into account bad words
    else:
        return "The word doesn't exist. Please double check it."

word=input("Enter word: ")

output=(translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

