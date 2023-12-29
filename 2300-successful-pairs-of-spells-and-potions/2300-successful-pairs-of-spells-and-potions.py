class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        
        res = []
        potions.sort()
        
        for i in spells:
            #binary search
            l,r = 0, len(potions)-1
            index = len(potions) # weakest potion value to calculate the count
            
            while l<=r:
                mid = (l + r) //2 
                
                if i * potions[mid] >= success:
                    r = mid - 1
                    index = mid
                else:
                    l = mid +1
            
            res.append(len(potions) - index)
            
        return res
        
#         res = []
#         for i in range(len(spells)):
#             count = 0
#             for j in range(len(potions)):
                
#                 if spells[i] * potions[j] >= success:
#                     count +=1
            
#             res.append(count)
            
        
#         return res


                
        