class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        res = 0
        
        l = 0
        r =len(height)-1
        
        while l <r:
            
            area = (r-l)*(min(height[l],height[r]))
            res = max(res,area)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return res     
        
        #brute force
#         res = 0
        
#         for l in range(len(height)):
#             for r in range(l+1,len(height)):
                
#                 area= (r-l)*(min(height[l],height[r]))
#                 res = max(res,area)
        
#         return res