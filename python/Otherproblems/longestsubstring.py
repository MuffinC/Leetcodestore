def lengthOfLongestSubstring(s):
    chase=set()
    l=0
    res=0
    for r in range(len(s)):
        while s[r] in chase:
            #update the window
            chase.remove(s[l]) #remove left most
            l+=1
        chase.add(s[r])
        res=max(res, r-l+1)
    return res
print(lengthOfLongestSubstring("qrsvbspk"))