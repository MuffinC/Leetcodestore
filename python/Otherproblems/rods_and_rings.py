def countPoints( rings):
    strings=list(rings)
    stack={}
    count=0
    for x in range(1,len(strings),1):
        #for rod numbers
        if x%2==1:
            if strings[x] not in stack:
                stack[strings[x]]=[strings[x-1]]
            else:
                key=strings[x]
                stack[key].append(strings[x-1])


    for y in stack.values():
        if 'B' in y:
            if 'R' in y:
                if 'G' in y:
                    count+=1

    return count



print(countPoints("B0R0G0R9R0B0G0"))