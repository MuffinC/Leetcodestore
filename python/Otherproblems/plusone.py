def plusOne(digits):
    totaltens=len(digits)-1
    total =0
    stack = []
    for x in digits:
        total = total + (x*10**totaltens)
        totaltens -=1
    total+=1
    for y in range(0,len(str(total)),1):
        stack.insert(-y,total%10)
        total = int(total/10)
    return stack






print(plusOne([9]))