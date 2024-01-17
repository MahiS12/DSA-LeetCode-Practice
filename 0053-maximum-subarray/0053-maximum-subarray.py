class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [0]* (len(nums))
        
        dp[0]= nums[0]
        maxSum = nums[0]
        
        for i in range(1,len(nums)):
            
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            maxSum = max(maxSum,dp[i])
        
        return maxSum
        
        
#         currSum = 0
#         maxSum = float("-inf")
        
#         for i in range(len(nums)):
#             currSum += nums[i]
            
#             if currSum > maxSum:
#                 maxSum = currSum
#             if currSum < 0:
#                 currSum = 0
        
#         return maxSum
            

