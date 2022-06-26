def spin_words(sentence):
    sent = sentence.split()
    res=[]
    for x in sent:
        if len(x)>=5:
            res.append(x[::-1])
        else: res.append(x)
    return " ".join(res)




print(spin_words("Hey fellow warriors"))