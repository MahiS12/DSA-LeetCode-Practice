class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        
        if m == 0:
            return 0  # empty needle
        
        for i in range(n - m + 1):
            found = True
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    found = False
                    break
            if found:
                return i
        return -1  # needle not found