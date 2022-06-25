def fizzBuzz(n):
    res=[]

    for x in range(1,n+1):
        if x%3==0:
            if x % 5 == 0:res.append("FizzBuzz")
            else: res.append("Fizz")
        elif x%5==0:res.append("Buzz")
        else: res.append(str(x))
    return res



print(fizzBuzz(15))