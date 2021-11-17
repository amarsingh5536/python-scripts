import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def thankyou():
    print("thank you")
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:  # in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


def call(x):


    output = translate(x)
    if type(output) == list:
        for item in output:
            print(item)
        callback()

    else:
        print(output)


def callback():
    word = input("Enter word or press y to exit: /n ")
    if word!="y":
        call(word)
    else:
        thankyou()
call(x = input("Enter word: "))