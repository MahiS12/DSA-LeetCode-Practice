class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        visited = []
        def zeroes(row,col):
            
            for i in range(0,len(matrix[0])):
                matrix[row][i]=0
                
            for j in range(0,len(matrix)):
                matrix[j][col]=0
        
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j]==0:
                    visited.append((i,j))
                    
        for i,j in visited:
            zeroes(i,j)
        