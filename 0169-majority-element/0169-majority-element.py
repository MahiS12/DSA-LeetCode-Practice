class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        count = 1
        majority = nums[0]

        for num in nums[1:]:
            if num != majority:
                count -= 1
                if count == 0:
                    majority = num
                    count = 1
            else:
                count += 1

        return majority    
        
        
        
        
        
        
        
        
        # d ={}
        
#         for i in nums:
#             if i not in d:
#                 d[i] = 1
#             else:
#                 d[i] +=1
            
        
#         return max(d, key = lambda x:d[x])
    
        
        