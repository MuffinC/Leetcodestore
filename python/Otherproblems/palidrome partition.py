def partition( s) :
    ans = []

    # cur will be the array for current tree
    def backtrack(cur, word1, partition2):
        if partition2 !=len(s) and word1 == word1[::-1]: cur.append(word1)
        elif partition2 ==len(s): cur.append(s[-1])

        while partition2 + 1 <= len(s):
            backtrack(cur, s[partition2:partition2 + 1], partition2+1)
            partition2+=1
        return

    partition1 = 1

    while partition1 < len(s):
        cur = []

        backtrack(cur, s[:partition1], partition1)
        ans.append(cur)
        partition1 += 1
    return ans

print(partition("aab"))