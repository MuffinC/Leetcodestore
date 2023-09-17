from collections import Counter
def minSwaps(data):
    table = Counter(data)
    if table[1] == 1: return 0

    l, r = 0, len(data) - 1
    swaps = 0
    while l < r:
        if data[l] == 1:
            l += 1
        elif data[r] == 1:
            swaps += 1
            hold = data[l]
            data[l] = data[r]
            data[r] = hold
            r -= 1
        else:
            r -= 1

    return swaps

print(minSwaps([1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]))