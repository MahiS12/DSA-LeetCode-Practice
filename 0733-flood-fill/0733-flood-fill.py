class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        
        row = len(image)
        col = len(image[0])
        ini = image[sr][sc]
        
        if ini == color:
            return image
        
        q = [(sr,sc)]
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
  
        new = image
        
        while q:
            
            x,y = q.pop(0)
            
            if new[x][y] == ini:
                new[x][y] = color
                
                for dr,dc in directions:
                    
                    nx = dr + x
                    ny = dc + y
                    
                    if nx >=0 and ny >=0 and nx < row and ny < col and new[nx][ny]==ini:
                        q.append((nx,ny))
        
        return new
                    
            