def hammingWeight(n):
    total = 0
    stringer = str(n)
    for x in stringer:
        if x == '1':
            total += 1
    return total


print(hammingWeight(0o0000000000000000000000000001011))