class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # unique = 0
        # for i in nums:
        #     unique ^= i
        # return unique

        low = 0
        high = len(nums)-1

        while low < high:
            mid = low +(high-low)//2

            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]

            #if middle is at odd index and same number present on left or even and right index
            if (mid%2 == 1 and nums[mid] == nums[mid-1]) or (mid%2==0 and nums[mid+1]==nums[mid]): 
                low= mid+1
            else:
                high= mid -1
        return nums[low]



            



        