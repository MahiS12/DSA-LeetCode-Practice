class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high= 0, len(nums)-1
        mini= nums[0]
        while low <high:
            mid= low + (high-low)//2
            if nums[low] < nums[high]:
                return nums[low]
            # if nums[mid]== target:
            #     return mid
            if nums[mid] >= nums[low]:
                low= mid+1
            else:
                high = mid
        return nums[low]
