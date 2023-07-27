class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        arr = []* n
        arr.append(nums[0])
        maxSum = nums[0]
        
        for i in range(1,n):
            arr.append(max(arr[i-1]+nums[i],nums[i]))
            
            if arr[i] > maxSum:
                maxSum = arr[i]
        
        return maxSum
            
            

        
#         curr = summax = nums[0]
        
#         for i in range(len(nums)-1):
#             curr = max(curr+nums[i+1], nums[i+1])
#             summax = max(curr,summax)
#         return summax
