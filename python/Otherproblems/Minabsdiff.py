def minimumAbsDifference(arr):
    stack = []
    stack2 = []
    out = []

    for x in range(0,len(arr),1):
        if len(arr)==1 or x == len(arr)-1:
            break
        for y in range(x+1,len(arr),1):
            if(y == len(arr)):
                break
            else:
                check = abs(arr[x] - arr[y])
                stack2.append([x,y])
                stack.append(check)
    res=min(stack)
    for x in range(0,len(stack),1):
        if (stack[x] == res):
             if (arr[stack2[x][0]]> arr[stack2[x][1]]):
                out.append([arr[stack2[x][1]],arr[stack2[x][0]]])
             else:
                 out.append([arr[stack2[x][0]], arr[stack2[x][1]]])




    return out



print(minimumAbsDifference([4,2,1,3]))