class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        d1 = {}
        d2 = {}
        res=0
        #frequency of s
        for i in s:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        #frequency of t        
        for i in t:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
                
        for j in d1.keys():
            if j in d2:
                if d1[j] > d2[j]:
                    res+= d1[j]-d2[j]
            else:
                res +=d1[j]
        
        return res

        