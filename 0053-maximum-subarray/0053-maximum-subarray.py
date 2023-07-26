class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        
        curr = summax = nums[0]
        
        for i in range(len(nums)-1):
            curr = max(curr+nums[i+1], nums[i+1])
            summax = max(curr,summax)
        return summax
        