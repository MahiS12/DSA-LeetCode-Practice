class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.rstrip()
        return len(s.split()[-1])
        
#         class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         cnt = 0;
#         for i in range(len(s)-1,-1,-1):
#             if(s[i]== ' '):
#                 if cnt>0 :
#                     return cnt
#                 continue
#             cnt+=1;
#         return cnt
# 2.

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s = s.rstrip()  #or strip
#         return len(s.split()[-1])
            
            
        
        
        