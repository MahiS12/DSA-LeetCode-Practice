class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        major = 0
        
        for i in range(len(nums)):
            if count ==0:
                major = nums[i]
                
            if nums[i] == major:
                count+=1
            else:
                count -=1
        
        return major
                
    
        
        
        
        
        
        
        
        
        # d ={}
        
#         for i in nums:
#             if i not in d:
#                 d[i] = 1
#             else:
#                 d[i] +=1
            
        
#         return max(d, key = lambda x:d[x])
    
        
        