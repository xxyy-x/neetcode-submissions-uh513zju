class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROW = len(grid)
        COL = len(grid[0])

        visit = set()
        res = 0        

        def dfs(r, c):
            if (c < 0 or r < 0 or c == COL or r == ROW):
                return 

            if grid[r][c] != '1':
                return
            
            if (r,c) in visit:
                return

            visit.add((r,c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for c in range(COL):
            for r in range(ROW):
                if grid[r][c] == '1' and (r,c) not in visit:
                    res +=1
                    dfs(r,c)

        return res






