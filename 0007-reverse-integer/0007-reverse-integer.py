class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            reverse = reverse * 10 + x % 10
            x //= 10
        result = sign * reverse
        if result > 2 ** 31 - 1 or result < -(2 ** 31):
            return 0
        return result
