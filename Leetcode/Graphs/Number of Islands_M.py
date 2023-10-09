class Solution(object):
    def numIslands(self, grid):
        visit=set()
        res=0
        def bfs(row,col):
            q=[(row,col)]
            visit.add((row,col))
            while q:
                r,c=q.pop(0)
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    i,j=dr+r,dc+c
                    if (i in range(len(grid)) and
                    c in range(len(grid[0])) and
                    (i,j) not in visit and
                    grid[r][c]=='1'):
                        visit.add((i,j))
                        q.append((i,j))
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=='1' and (r,c) not in visit:
                    bfs(r,c)
                    res+=1
        return res