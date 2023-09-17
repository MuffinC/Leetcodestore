class Solution:
    def makePalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        k=2
        while l<r:
            if s[l]==s[r]:
                r-=1
                l+=1
            elif s[l]!= s[r]:
                k-=1
                r-=1
                l+=1


        return k>=0