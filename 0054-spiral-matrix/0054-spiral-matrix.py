class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        #O(m*n)
        
        res = []
        
        left,right = 0, len(matrix[0]) #right given columns
        top, bottom = 0, len(matrix) #bottom gives rows
        
        while left < right and top < bottom:
            
            #top row
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1
            #right column
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right-=1
            
            #edge case
            if not(left<right and top <bottom):
                break
            
            #bottom row
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom-=1
            #left column
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left+=1
            
        return res