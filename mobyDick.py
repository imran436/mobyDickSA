def getStopWords():
       f = open("stop-words.txt")
    firstSplit = f.read().split('#')
    words = firstSplit[len(firstSplit)-1]
    words = words.splitlines()
    words = list(filter(None, words))
    print(words)
def getBook():
    pass
def removeStopWords():
    pass
def count():
    pass
