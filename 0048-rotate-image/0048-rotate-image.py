class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix[0])
        #transpose
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #reverse
        for i in range(n):
            low=0
            high = n-1
            while low <high:
                matrix[i][low], matrix[i][high]= matrix[i][high], matrix[i][low]
                low +=1
                high-=1
        

