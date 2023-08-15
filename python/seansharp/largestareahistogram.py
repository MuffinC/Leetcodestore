def ans(heights):
    maxarea=0
    stack=[] #pair (index,height)
    for x,y in enumerate(heights):
        start=x
        while stack and stack[-1][1] >y:
            index,height =stack.pop()
            maxarea=max(maxarea,height*(x-index))
            start=index
        stack.append((start,y))
    #excess entries

    for x,y in stack:
        maxarea=max(maxarea, y *( len(heights) -x))
    return maxarea

print(ans([2,1,5,6,2,3]))


