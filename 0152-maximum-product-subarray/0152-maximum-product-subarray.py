class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        currentMin, currentMax = 1,1
        res = nums[0]
        
        for i in nums:
            temp = i*currentMax
            currentMax= max(i,i*currentMax,i*currentMin)
            currentMin = min(temp,i,i*currentMin)
            res = max(res,currentMax)
        
        return res
