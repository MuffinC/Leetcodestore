class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms)==1: return True

        
        
        seen=set()
        
        def dfs(room):
            seen.add(room)
            for x in rooms[room]:
                if x not in seen:
                    dfs(x)
        dfs(0)


        return len(seen) == len(rooms)

