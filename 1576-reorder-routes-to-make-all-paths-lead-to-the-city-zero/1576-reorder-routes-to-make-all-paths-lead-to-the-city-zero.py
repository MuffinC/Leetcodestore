class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        
        #start at city0
        # recusrivelyy check neighbours
        # count outgoing edges

        edges= {(a,b) for a,b in connections}
        neighbours={city:[] for city in range(n)}
        visit=set()
        changes =0

        for a,b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)

        def dfs(city):
            nonlocal edges, neighbours, visit, changes

            for neighbour in neighbours[city]:
                if neighbour in visit: continue
                #check if neighbnour can reach city 0
                if(neighbour,city) not in edges:
                    changes+=1
                visit.add(neighbour)
                dfs(neighbour)
        visit.add(0)
        dfs(0)

        return changes


