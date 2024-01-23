class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        hashmap = {}
        
        for i in arr:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        
        new = sorted(i for i in hashmap.values())
        
    
        for j in range(len(new)):
            if new[j] == new[j-1] and j!=0:
                return False
        
        return True