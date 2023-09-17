class SmallestInfiniteSet:

    def __init__(self):
        self.cur=1
        self.s =set()
        

    def popSmallest(self) -> int:
        if self.s:
            res=min(self.s)
            self.s.remove(res)
            return res
        #if the set is empty take the last known value and incremenet it and return, but u still are moving on
        else:
            self.cur +=1
            return self.cur-1

        

    def addBack(self, num: int) -> None:
        if self.cur>num:
            self.s.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)