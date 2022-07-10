import re
from collections import Counter
import tkinter as tk
from tkinter import *
def getStopWords():
    f = open("stop-words.txt")
    stopWords = f.read().split('#')
    stopWords = stopWords[len(stopWords)-1]
    stopWords = stopWords.splitlines()
    stopWords = list(filter(None, stopWords))
    stopWords = list(map(lambda x: x.lower(), stopWords))
    f.close()

    return stopWords
def getBook():
    f = open("mobydick.txt", encoding="utf-8")
    words = re.sub(r'[^\w\s]', "", f.read()).split()
    f.close()
    words = list(map(lambda x: x.lower(), words))
    return words
def removeStopWords(words, stopwords):
    newList = [x for x in words if x not in stopwords]
    return newList
def count(wordList):
    c = Counter(wordList)
    top100 =[]
    for x in c.most_common(100):
        top100.append(x[0])
    return top100
def runProgram():
    txt.delete('1.0', tk.END)
    index = 1
    for word in count(removeStopWords(getBook(), getStopWords())):
        txt.insert(tk.END,  "{}. ".format(index) +word +"\n")
        index+=1

root = Tk()
root.title("Moby Dick Word Counter")
root.geometry('450x500')

frame1 = tk.Frame()
lbl = Label(root, text = "Find the top 100 most frequently occuring words in moby dick")
lbl.pack()
btn = Button(root, text="Start the Count", command=runProgram)
btn.pack()

frame2 = tk.Frame()
txt = tk.Text()
txt.pack()

frame1.pack()
frame2.pack()

root.mainloop()
