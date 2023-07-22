class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        time, fresh = 0,0
        row = len(grid)
        col = len(grid[0])
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        
        while q and fresh >0:
            
            for i in range(len(q)):
                r,c = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                
                for dr,dc in directions:
                    nr = dr + r
                    nc = dc + c
                    
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append([nr,nc])
                        fresh -=1
                    
            time+=1
        
        return time if fresh ==0 else -1
                
            
        