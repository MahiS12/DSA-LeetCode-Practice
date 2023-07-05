class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        low =0
        high= len(nums)-1

        while low <  high:
            mid= low +(high-low)//2

            if mid ==0:
                return 0 if nums[0] >= nums[1] else 1
            if mid == high:
                return high-1 if nums[high-1] >= nums[high-2] else high-2

            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid-1]:
                low = mid+1
            else:
                high = mid-1
        return low
    
    
#         while low <high:
            
#             mid = low +(high-low)//2
            
#             if nums[mid] > nums[mid+1]:
#                 high = mid
#             elif nums[mid] > nums[mid-1]:
#                 low = mid+1
                
#         return low
                
         
    

