class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # i= j = 0
        # while j <= len(nums2):
        #     if nums1[i] <= nums2[j]:
        #         i+=1
        #     else:
        #         nums1[i+1] = nums1[i]
        #         nums1[i] = nums2[j]
        #         j+=1

        i = m-1
        j = n-1
        index = m + n -1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i-=1
            else:
                nums1[index] = nums2[j]
                j-=1
            index -=1
