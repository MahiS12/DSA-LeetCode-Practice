class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1 or n==2:
            return n
        
        prev = curr =1
        
        for i in range(2,n+1):
            temp = curr
            curr=curr+prev
            prev=temp
        return curr
            
        
        
#         dp=[0]*(n+1)
#         dp[1]=1
#         dp[2]=2
        
#         for i in range(3,n+1):
#             dp[i]=dp[i-1]+dp[i-2]
        
#         return dp[n]