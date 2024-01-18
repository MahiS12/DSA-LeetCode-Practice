class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2
     
#         dp=[0]*(n+1)
#         dp[1]=1
#         dp[2]=2
        
#         for i in range(3,n+1):
#             dp[i]=dp[i-1]+dp[i-2]
        
#         return dp[n]