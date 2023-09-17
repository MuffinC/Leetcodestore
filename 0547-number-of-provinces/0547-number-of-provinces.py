class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        
        provinces=0

        visited = [False] * (len(M))

        def dfs(node):
            visited[node] = True
            for x in range(0, len(visited)):
                if M[node][x] == 1 and visited[x] == False:
                    dfs(x)


        for y, x in enumerate(visited):
            if x == False:
                dfs(y)
                provinces += 1

        return provinces