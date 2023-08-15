def minWindow(s: str, t: str) -> str:
    if t == "": return ""
    window, needT = {}, {}
    have, need = 0, len(t)
    left = 0

    res, reslen = [-1, -1], float("inf")

    # hashtables to compare to
    for x in t:
        needT[x] = 1 + needT.get(x, 0)

    for r in range(len(s)):
        cur = s[r]  # current element
        window[cur] = 1 + window.get(cur, 0)  # creates the window table while appending result

        if (cur in needT) and window[cur] == needT[cur]:
            have += 1

        while have == need:
            # to extract and push the left pointer to new unit

            # check if current window length is < the current minlen
            if (r - left + 1) < reslen:
                res = [left, r]
                reslen = r - left + 1

            # pop from the left
            window[s[left]] -= 1
            # by removing a character, we need to update the have counter if there is a change
            if s[left] in needT and window[s[left]] < needT[s[left]]:
                have -= 1
            left += 1
    l, r = res

    return s[l:r + 1] if reslen != float("infinity") else ""

print(minWindow("aa","aa"))