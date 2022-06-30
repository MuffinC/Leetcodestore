def dailyTemperatures(temperatures):
    res=[0]*len(temperatures)
    stack=[] #(temp,index)

    for x,y in enumerate(temperatures):
        while stack and y>stack[-1][0]:
            stacktemp,stackindex = stack.pop()
            res[stackindex] = x-stackindex
        stack.append([y,x])


    return res


print(dailyTemperatures([55,38,53,81,61,93,97,32,43,78]))
