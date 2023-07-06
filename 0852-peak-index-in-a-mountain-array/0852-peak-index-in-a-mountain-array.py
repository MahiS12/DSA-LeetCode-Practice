class Solution(object):
    def peakIndexInMountainArray(self, nums):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        
        low =0
        high= len(nums)-1

        while low <  high:
            mid= low +(high-low)//2

            if nums[mid] < nums[mid+1]:  #look in the right half
                low = mid+1
            elif nums[mid] > nums[mid+1]: #look in the left half
                high = mid
        return low
    