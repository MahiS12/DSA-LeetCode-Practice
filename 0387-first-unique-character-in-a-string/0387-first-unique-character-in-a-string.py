class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
        hashmap = {}
        
        for i in s:
            hashmap[i] = 1 + hashmap.get(i,0)
        
        
        for i in range(len(s)):
            
            if hashmap[s[i]] ==1:
                return i
        
        return -1
            
                