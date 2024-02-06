class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        l = 0
        n = len(nums)
        r = n -1
        i = 0
        
        while i <n and i <=r:
            
            if nums[i] == 0:
                nums[i],nums[l] = nums[l], nums[i]
                l+=1
                i+=1
            
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r-=1
            
            else:
                i+=1
        
        
        