import json
import difflib

data = json.load(open('data.json'))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        word1 = difflib.get_close_matches(word, data.keys())
        if len(word1)>0:
            print(f"Did you mean {word1[0].capitalize()}? Showing search for {word1[0].capitalize()}")
            return data[word1[0]]
        else:
            print("Word dosent exists  . . . .")
            return ''

print('Enter /end to exit')
while True:
    i=1
    word = input("Enter Word : ")
    if word == '/end':
        break
    out = translate(word)
    for dat in out:
        print(f"{i}: {dat}")
        i=i+1