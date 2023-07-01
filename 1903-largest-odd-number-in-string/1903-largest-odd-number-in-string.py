class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        i = len(num)-1
        while i >= 0:
		    if int(num[i]) % 2:
			    return num[:i + 1]
		    i-= 1
        return ""