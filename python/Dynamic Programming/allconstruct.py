def allConstruct(target,words,memo={}):
    if target =='': return [[]]
    result=[]
    for x in words:
        if target.startswith(x):
            suffix=target[len(x):]

            sufways=allConstruct(suffix,words,memo)
            targetways=sufways.insert(0,x)
            result.append(targetways)
    return result





print(allConstruct('purple',['purp','p','ur','le','purpl']))
#print(allConstruct('abcdef',['ab','abc','cd','def','abcd','ef','c']))