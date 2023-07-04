class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        
        
        def helper(num,count):
            
            if num ==0:
                return count
            
            if num % 2 ==0:
                return helper(num//2,count+1)
            
            return helper(num-1,count+1)
        
        return helper(num,0)
        