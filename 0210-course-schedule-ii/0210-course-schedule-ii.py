class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        #create a pre req table: initial node||Prereq array
        table ={x:[] for x in range(numCourses)}
        for x, y in prerequisites:
            table[x].append(y)
            
            
        output=[]
        visit,cycle =set(), set()
        
        def dfs(crs):
            if crs in cycle: return False
            if crs in visit: return True
            
            cycle.add(crs)
            for pre in table[crs]:
                if dfs(pre) == False: return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
            
            
            
            
            
            
            
        for x in range(numCourses):
            if dfs(x) == False: return []
            
        return output
            
            