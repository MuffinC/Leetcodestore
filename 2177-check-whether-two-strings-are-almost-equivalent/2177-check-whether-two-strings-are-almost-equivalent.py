class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        word1c=Counter(word1)
        word2c=Counter(word2)
        for x in word1c:
            if x not in word2c:
                word2c[x]=0
            if abs(word1c[x] -word2c[x])>3:
                return False

        for x in word2c:
            if x not in word1c:
                word1c[x]=0
            if abs(word1c[x] -word2c[x])>3:
                return False
            

        return True
        

