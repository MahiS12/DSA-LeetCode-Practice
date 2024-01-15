class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        row = [0] * (n-1) + [1]
        
        for i in range(m):
            for j in range(n-2, -1, -1):
                row[j] += row[j+1]
        
        return row[0]
    
#         row = [1] * n

#         for i in range(m - 1):
#             newRow = [1] * n
#             for j in range(n - 2, -1, -1):
#                 newRow[j] = newRow[j + 1] + row[j]
#             row = newRow
#         return row[0]

        # O(n * m) O(n)
        