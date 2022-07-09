import re
from collections import Counter
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
    print(c.most_common(100))
def runProgram():    
    count(removeStopWords(getBook(), getStopWords()))
