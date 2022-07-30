def longestPalindrome( s):
    # just need to cut inwards and check
    if len(s) < 1: return s
    if s[:] == "".join(list(reversed(s[:]))):
        return s[:]
    l, r = 1, len(s) - 1

    while (l < len(s)):

        if s[l:] == "".join(list(reversed(s[l:]))):
            return s[l:]

        if s[:r] == "".join(list(reversed(s[:r]))):
            return s[:r]

        if s[l:r] == "".join(list(reversed(s[l:r]))):
            return s[l:r]
        l += 1
        r -= 1
    return -1


print(longestPalindrome("cbbd"))
