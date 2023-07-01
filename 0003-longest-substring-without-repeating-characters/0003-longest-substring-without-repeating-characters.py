class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        res=left = 0
        hashSet = set()

        for right in range(len(s)):
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left +=1
            hashSet.add(s[right])
            res= max(res, right-left+1) #current window
        return res

        
