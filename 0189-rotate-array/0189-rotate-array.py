class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if k == n or k == 0:
            return
        k= k % n
        if k > n:
            return
        temp= [None]*n
        for i in range(n-k):
            temp[i]= nums[i]
        for i in range(k):
            nums[i]=nums[i+n-k]
        for i in range(k,n):
            nums[i]=temp[i-k]
            

            

