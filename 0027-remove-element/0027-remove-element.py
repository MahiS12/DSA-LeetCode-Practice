class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = i  = 0
        
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                count +=1
        return count
            
                