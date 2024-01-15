class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == " ":
            return True

        alnum_letters = [i.lower() for i in s if i.isalnum()]

        L = 0
        R = len(alnum_letters) - 1

        while L <= R:
            if alnum_letters[L] == alnum_letters[R]:
                L += 1
                R -= 1
            else:
                return False

        return True
        
#         new = ''
#         for a in s:
#             if a.isalpha() or a.isdigit():
#                 new += a.lower()
#         return (new == new[::-1])
        