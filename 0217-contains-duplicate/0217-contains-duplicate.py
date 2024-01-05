class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashset = set()
        
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False
        
        
#         nums.sort()
        
#         for i in range(1,len(nums)):
#             if nums[i-1]==nums[i]:
#                 return True
#         return False
        
        
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
                
#                 if nums[i] == nums[j]:
#                     return True