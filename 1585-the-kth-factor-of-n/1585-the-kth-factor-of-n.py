class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res=[]
        for x in range(1,n+1):
            if n%x ==0:
                res.append(x)
        print(res)
        if len(res)<k: return -1
        return res[k-1]
            
        