def wordPattern(pattern, s):
    #first split it
    words=s.split(" ")
    if len(pattern)!=len(words):return False

    #hashmap
    chartoWord={}
    wordtoChar={}

    for c,w in zip(pattern,words):
        if c in chartoWord and chartoWord[c]!=w:
            return False
        if w in wordtoChar and wordtoChar[w]!=c:
            return False

        #add to the hashmap
        chartoWord[c] = w
        wordtoChar[w] = c

    return True
print(wordPattern("abba","dog cat cat dog"))