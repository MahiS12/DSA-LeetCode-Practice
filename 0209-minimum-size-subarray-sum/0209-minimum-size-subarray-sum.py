class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        i, current = 0,0
        count = len(nums)+1
        
        for j in range(len(nums)):
            current += nums[j]
            while current >= target:
                count = min(count,j-i+1)
                current -= nums[i]
                i+=1
            
        return 0 if count == len(nums)+1 else count
        
        
#         i = 0
#         count = len(nums) +1


#         for j in range(len(nums)):
#             while sum(nums[i:j+1]) >= target:
#                 count = min(count,j-i+1)
#                 i+=1
                
#         if count == len(nums)+1:
#             return 0
#         else:
#             return count
        
