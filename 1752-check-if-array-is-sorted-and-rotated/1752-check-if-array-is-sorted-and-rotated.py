class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n= len(nums)
        count = 0
        if n <= 1:
            return True
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                count +=1
            if count > 1:
                return False
        if count==1 and nums[0] < nums[n-1]:
            return False
        return True 
