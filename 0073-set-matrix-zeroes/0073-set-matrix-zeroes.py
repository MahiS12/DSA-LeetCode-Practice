class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows,cols = len(matrix), len(matrix[0])
        rowZero = False
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    
                    matrix[0][c]=0
                    if r > 0:
                        matrix[r][0]=0
                    else:
                        rowZero= True
        
        
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][0] ==0 or matrix[0][c]==0:
                    matrix[r][c]=0
        
        if matrix[0][0]==0:
            for r in range(rows):
                matrix[r][0]=0
        
        if rowZero:
            for c in range(cols):
                matrix[0][c]=0
        
        
#         visited = []
#         def zeroes(row,col):
            
#             for i in range(0,len(matrix[0])):
#                 matrix[row][i]=0
                
#             for j in range(0,len(matrix)):
#                 matrix[j][col]=0
        
#         for i in range(0,len(matrix)):
#             for j in range(0,len(matrix[0])):
#                 if matrix[i][j]==0:
#                     visited.append((i,j))
                    
#         for i,j in visited:
#             zeroes(i,j)
        