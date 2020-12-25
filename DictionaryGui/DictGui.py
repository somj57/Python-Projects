import json
import difflib
from tkinter import *
import sys
from os import path
import os
path_to_dat = path.join(os.path.dirname(sys.executable), 'data.json')


data = json.load(open(path_to_dat))

window=Tk("")
window.title("Dictionary")

def translate(word):
    word = word.lower()
    if word in data:
        disp = [word]
        men = data[word]
        com = [disp, men]
        return com
    else:
        word1 = difflib.get_close_matches(word, data.keys())
        if len(word1) > 0:

            disp = [f"Did you mean {word1[0].capitalize()}? Showing search for {word1[0].capitalize()}"]
            men = [disp, data[word1[0]]]
            return men
        else:
            # print("Word dosent exists  . . . .")
            return [['Try entering something else '], ['']]

def kmToMiles():
    t1.delete(1.0,END)
    #print(e1_value.get())
    miles = translate(e1_value.get())
    var1=miles[0]
    var2=miles[1]
    e1.delete(0, 'end')
    for i in var1:
        t1.insert(END, i+ '\n')
    for i in var2:
         t1.insert(END,i+'\n')

b1=Button(window,text="Search",command=kmToMiles)
b1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvar=e1_value)
e1.grid(row=0,column=1,rowspan=3)


t1=Text(window,height=6,width=60)
t1.grid(row=0,column=3)

#window.geometry("500x100")
window.mainloop()