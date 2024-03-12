def findLongestChain(pairs):
    pairs = sorted(pairs,  key=lambda x:x[1])
    if len(pairs) == 1: return 1

    start = pairs[0][0]
    end = pairs[0][1]
    ans = 1
    pairs.pop(0)
    for nstart, nend in pairs:
        if nstart > end:
            ans += 1
            end = nend
    return ans

print(findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]))