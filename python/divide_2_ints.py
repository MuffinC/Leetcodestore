def divide(dividend,divisor):
    count=0
    if(dividend<0 or divisor<0):
        for x in range(0,abs(dividend),abs(divisor)):
            count+=1
            if (dividend - x < divisor):
                count = count - 1
                break
        return -count

    else:
        for x in range(0,dividend,divisor):
            count+=1
            if(dividend-x<divisor):
                count=count-1
                break
        return count
print(divide(-12,3))