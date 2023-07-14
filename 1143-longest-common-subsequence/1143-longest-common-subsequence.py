class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        #bottom up approach
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
                    
        return dp[0][0]
    

        
#         m= len(text1)
#         n= len(text2)

#         def lcs(text1,text2,m,n):
#             if m == 0 or n == 0:
#                 return 0
#             elif text1[m-1] == text2[n-1]:
#                 return 1 + lcs(text1,text2,m-1,n-1)
#             else:
#                 return max(lcs(text1,text2,m-1,n),lcs(text1,text2,m,n-1))

#         return lcs(text1,text2,m,n)





        
            

        