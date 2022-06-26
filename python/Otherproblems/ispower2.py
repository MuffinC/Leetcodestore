def isPowerOfTwo(n):
    if n == 1:
        return True
    else:
        if n < 1:
            return False
        return isPowerOfTwo(n / 2)

    return isPowerOfTwo(n / 2)

print(isPowerOfTwo(3))