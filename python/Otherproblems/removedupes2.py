def removeDuplicates( s, k) -> str:
    stackcounter = [] #pair stack
    for x in s:
        if stackcounter and stackcounter[-1][0]==x: #this checks the top of the stack and the element if it matches
            stackcounter[-1][1]+=1
        else:
            stackcounter.append([x,1]) #new element introduction
        if stackcounter[-1][1]==k:
            stackcounter.pop() #remove the whole element by a single pop
    res=""
    for char,count in stackcounter:
        res +=(char *count)
    return res


print(removeDuplicates("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy",4))

