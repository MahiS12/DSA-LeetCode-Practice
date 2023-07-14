class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        res_L = 0
        res_R = 0
        resLen = 0
        
        for i in range(len(s)):
            
            #odd length
            l,r = i,i
            
            while l >= 0 and r < len(s) and s[l]== s[r]:
                
                if resLen < (r-l+1):
                    res_L = l
                    res_R = r
                    resLen = r - l + 1
                 
                l-=1
                r +=1
            
            #even length
            l,r = i, i+1
            
            while l >= 0 and r < len(s) and s[l]== s[r]:
                
                if resLen < (r-l+1):
                    res_L = l
                    res_R = r
                    resLen = r - l + 1
                 
                l-=1
                r +=1
            
        return s[res_L:res_R+1]
            
            
                
                