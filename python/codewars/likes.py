def likes(names):

    back = ' likes this'
    value = len(names)
    if value == 0: return 'no one' + back
    front = ""

    if value > 3: valx = value - 2

    for x, y in enumerate(names):
        if value == 1:
            return y + back
        elif value == 2:
            if x ==0: front=y + ' and '
            else: front=front + y + back
        elif value ==3:
            if x ==0: front=y + ', '
            elif x==1: front=front +y+' and '
            else: front=front + y + back
        else:
            if x ==0: front=front+y+', '
            else:
                front=front+y+ ' and '+str(valx)+' others like this'
                return front
    return front



print(likes(['Alex', 'Jacob', 'Mark', 'Max']))