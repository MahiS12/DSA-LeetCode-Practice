class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        i = j = count =0
        
        if len(s) > len(t):
            return False
        if len(s)== 0 or len(t) ==0:
            return True
        
        
        while j < len(t) and i <len(s):
            if s[i] == t[j]:
                i+=1
                count+=1
            j+=1
        
       
        if count >= len(s):
            return True
        else:
            return False