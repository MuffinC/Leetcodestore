def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    import collections
    ard = collections.Counter()
    largestCount, maxlen = 0, 0
    for x in range(len(s)):
        ard[s[x]] += 1
        largestCount = max(largestCount, ard[s[x]])
        if maxlen - largestCount >= k:
            ard[s[x - maxlen]] -= 1
        else:
            maxlen += 1
    return maxlen

print(characterReplacement("AABABBA",1))

