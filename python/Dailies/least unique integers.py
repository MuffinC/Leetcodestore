from collections import Counter
def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    table = Counter(arr)
    lister = []
    for x, y in table.items():
        lister.append([x, y])

    lister = sorted(lister, key=lambda x: x[1])
    cur = 0
    while cur < k:
        cur += lister[0][1]
        if cur <= k:
            lister.pop(0)

    return len(lister)

    return len(lister)

print(findLeastNumOfUniqueInts([5,5,4], 1))