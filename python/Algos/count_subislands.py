def subislands(grid1,grid2):
    #get the dimensions, both grids will be the same size
    rows,col = len(grid1),len(grid1[0])
    visit = set()


    #dfs
    def dfs(r,c):

        #grid2[r][c] == water
        if (r<0 or c<0 or r==rows or c==col or grid2[r][c] ==0 or (r,c) in visit):
            return True
        visit.add((r,c))# basically adding the island u already visited
        res = True

        if grid1[r][c] ==0:
            res=False #when it is water
        #all 4 directions and u are checking if it is water, the x and res is just to set false into res
        res = dfs(r+1,c) and res
        res = dfs(r-1, c) and res
        res = dfs(r, c+1) and res
        res = dfs(r, c-1) and res
        return res

    count = 0
    for r in range(rows):
        for c in range(col):
            #we are searching in grid2, if the grid2[r][c] is true + +run dfs again this means it is a dfs in island 1
            if grid2[r][c] and (r,c) not in visit and dfs(r,c):
                count+=1
    return count




print(subislands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))
