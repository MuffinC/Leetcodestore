def wordBreak(s, wordDict) :
    # deque=[0] starting indexes to pass through and check
    # word="" adds new letters in until u are part of the worddict.
    from collections import deque
    que = deque()
    que.append(0)

    seen = set()

    # find the max length in dict
    maxL = max(wordDict, key=len)
    print(maxL)

    l = 0
    while l < len(s):
        if not que: break
        l = que.popleft()
        if l >= len(s): break

        seen.add(l)
        cur = ""
        for x in range(l, l+maxL):
            if x >= len(s): break
            cur += s[x]
            if cur in wordDict:
                if x==len(s)-1: return True
                if x + 1 not in seen:
                    que.append(x + 1)



    if cur in wordDict: return True
    return False



print(wordBreak("cars",["car","ca","rs"]))