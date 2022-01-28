def addBinary(a, b):
    return str(bin(int(a,2)+int(b,2))[2:])


print(addBinary("111","1"))