def numKLenSubstrNoRepeats(s, k):
    from collections import Counter
    table = Counter()
    ans = 0
    s=list(s)
    for ind, letter in enumerate(s):
        table[letter] += 1
        if ind + 1 > k:
            table[s[ind - k]] -= 1
            if table[s[ind - k]]==0:
                table.pop(s[ind - k])
        if len(table) == k and sum(table.values()) == k: ans += 1

    return ans



print(numKLenSubstrNoRepeats("havefunonleetcode",5))