class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m = len(nums1)
        n = len(nums2)
        
        dp = [[0 for j in range(n+1)] for i in range (m+1)]
        
        res = 0
        
        for i in range(1,len(nums1)+1):
            for j in range(1,len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] > res:
                        res = dp[i][j]
        return res
        

        