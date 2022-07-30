def plusOne(digits):
    """
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


    """
    digits = [str(x) for x in digits]
    res = int("".join(digits)) +1
    return [x for x in list(str(res))]







print(plusOne([1,2,3]))