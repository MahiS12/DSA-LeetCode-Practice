class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        
        #one pointer
        merged = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])

        return "".join(merged)
    
    # double pointer
#         i,j = 0,0
#         result = []
        
#         while i < len(word1) and j < len(word2):
#             result.append(word1[i])
#             result.append(word2[j])
#             i+=1
#             j+=1
#         result.append(word1[i:])
#         result.append(word2[j:])
        
#         return "".join(result)