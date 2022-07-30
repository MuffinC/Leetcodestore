def reverseBits(n):
    ans = 0
    for i in range(32):
        ans = (ans << 1) + (n & 1)
        n >>= 1
    return ans


print(reverseBits(0b00000010100101000001111010011100))