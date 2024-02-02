class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        res = []
        
        string = "123456789"
        n = len(str(low))
        
        for i in range(n,10):
            for j in range(0,10-i):
                numStr = string[j:j+i]
                num = int(numStr)
                
                if low <= num <= high:
                    res.append(num)
        return res
        
#         res = []
        
#         for i in range(1,10):
#             num = i
#             next_digit = i+1
            
#             while num <= high and next_digit <=9:
#                 num = num*10 + next_digit
                
#                 if low <= num <= high:
#                     res.append(num)
#                 next_digit+=1
        
#         res.sort()
#         return res
        
#         res =[]
#         for i in range(low,high+1):
            
#             temp = str(i)
#             seq = True
            
#             for j in range(1,len(temp)):
                
#                 if int(temp[j]) != int(temp[j-1])+1:
#                     seq = False
#                     break
            
#             if seq:
#                 res.append(i)
        
        
#         return res
                
                
                
            