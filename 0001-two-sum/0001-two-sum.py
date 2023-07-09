class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]== target:
                    return [i,j]
    
            
            
            
            
#         hashmap={}
#         for i in range(len(nums)):
#             diff=target- nums[i]
#             if diff in hashmap:
#                 return [i,hashmap[diff]]
#             hashmap[nums[i]]=i
            
