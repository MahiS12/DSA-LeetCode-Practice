class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()
        
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                return True
        return False
        
        
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
                
#                 if nums[i] == nums[j]:
#                     return True