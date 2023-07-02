class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        count = 1
        major = nums[0]
        
        for i in nums[1:]:
            if i != major:
                count -=1
                if count ==0:
                    major = i
                    count =1
            else:
                count+=1
        return major
        
        
        
        
        
        
        
        
        # d ={}
        
#         for i in nums:
#             if i not in d:
#                 d[i] = 1
#             else:
#                 d[i] +=1
            
        
#         return max(d, key = lambda x:d[x])
    
        
        