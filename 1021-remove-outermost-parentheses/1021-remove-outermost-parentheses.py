class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 0:
            return ""
        s1 = ""
        count = j = 1
        i =0

        while j < len(s):
                if s[i] == '(' and s[j] == '(':
                    count+=1
                    j +=1
                if s[i] == '(' and s[j] == ')':
                    if count != 1:
                        j +=1
                        count -=1
                    else:
                        count -=1
                        s1 = s1 + s[i+1:j]
                        i = j+1
                        j+=1
        
        return s1


                