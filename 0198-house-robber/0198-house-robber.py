class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prev2=0
        prev = nums[0]
        
        for i in range(1,len(nums)):
            taken = nums[i] +prev2
            nottaken = prev
            curr = max(taken,nottaken)
            prev2=prev
            prev=curr
        
        return prev