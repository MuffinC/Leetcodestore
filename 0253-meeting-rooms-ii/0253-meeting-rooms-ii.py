class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms=0
        if not intervals:return 0
        endp=0

        starters=sorted([x[0]for x in intervals])
        ends=sorted([x[1]for x in intervals])

        #[0,5,15]
        #[10,20,30]

        for i in range(len(starters)):
            if starters[i]>=ends[endp]:
                endp+=1
            else:
                rooms+=1
        
        return rooms