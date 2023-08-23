class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        anslen=0

        for x in range(len(s)):
            #odd check
            l,r= x,x
            while l>=0 and r<len(s) and s[l] ==s[r]:
                #update the counter
                if (r-l +1)> anslen:
                    ans=s[l:r+1]
                    anslen=r-l +1
                l-=1
                r+=1


            #even check
            l,r=x,x+1
            while l>=0 and r<len(s) and s[l] ==s[r]:
                #update the counter
                if (r-l +1)> anslen:
                    ans=s[l:r+1]
                    anslen=r-l +1
                l-=1
                r+=1
        return ans