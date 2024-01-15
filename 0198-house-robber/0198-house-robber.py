class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0]*len(nums)
        dp[0]= nums[0] #prev
        
        for i in range(1,len(nums)):
            taken = nums[i]
            if i>1:
                taken = nums[i] + dp[i-2]
            nottaken = dp[i-1]
            dp[i]= max(taken,nottaken)
        
        return dp[len(nums)-1]
                       
#         prev2=0
#         prev = nums[0]
        
#         for i in range(1,len(nums)):
#             taken = nums[i] +prev2
#             nottaken = prev
#             curr = max(taken,nottaken)
#             prev2=prev
#             prev=curr
        
#         return prev
    
        
        