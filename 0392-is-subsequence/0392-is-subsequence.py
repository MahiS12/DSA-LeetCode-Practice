class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
#         i,j = 0,0
#         n,m = len(t), len(s)
#         if m == 0:
#             return True
        
#         overlap = 0
#         while i < n and j < m:
#             if t[i] == s[j]:
#                 i += 1
#                 j += 1
#                 overlap += 1
#             else:
#                 i += 1
#         return overlap == m
        
        
        i = j = count =0
        
        if len(s) == 0:
            return True
        
        while j < len(t) and i <len(s):
            if s[i] == t[j]:
                i+=1
                count+=1
            j+=1
            
        return count == len(s)
        
       
        # if count >= len(s):
        #     return True
        # else:
        #     return False





        