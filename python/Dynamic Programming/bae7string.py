def convertToBase7(num):
    """
    :type num: int
    :rtype: str
    """

    remainder = num%7
    tens =10

    rounds=1
    while(1):
        if(num%7 ==0):
            result = num // 7
            if (result%7 !=0) and (result >7):
                return "fail"
            else:
                out=rounds*(result)
                return str(out)
        else:
            out =num
            return str(out)



print(convertToBase7(100))
#100=202