def getStopWords():
    f = open("stop-words.txt")
    firstSplit = f.read().split('#')
    words = firstSplit[len(firstSplit)-1]
    words = words.splitlines()
    stopWords = list(filter(None, words))
    f.close()
def getBook():
    f = open("mobydick.txt", encoding="utf-8")
    words = re.sub(r'[^\w\s]', "", f.read()).split()
    f.close()
    return words
def removeStopWords():
    pass
def count():
    pass
