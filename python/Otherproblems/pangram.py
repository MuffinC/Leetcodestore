def checkIfPangram(sentence):
    #Alphabet:count?
    sent=sorted(sentence)
    if(len(sent))<25:return False
    count=0
    for x in range(0,len(sent)-1,1):
        if ord(sent[x+1])-ord(sent[x])>=2:
            return False
        if (ord(sent[x+1])-ord(sent[x]))!=0:
            count+=1
        if count == 25:
            return True

    return False




print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))