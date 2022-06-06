def numJewelsInStones(jewels, stones):

    jew=list(jewels)
    sto=list(stones)
    storage={} #jew:counter
    counter=0
    for x in jew:
        storage[x]=0

    for y in sto:
        if y in storage.keys():
            counter+=1

    return counter


print(numJewelsInStones("aA","aAAbbbb"))