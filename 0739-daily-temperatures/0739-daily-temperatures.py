class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]* len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            
            while stack and temperatures[i] > temperatures[stack[-1]]:
                t = stack.pop()
                res[t] = i -t
            
            stack.append(i)
        
        return res
                
        
        
        
        
        

#         res = [0] * len(temperatures)  # Initialize with 0s
    
#         for i in range(len(temperatures)):
#             for j in range(i + 1, len(temperatures)):
#                 if temperatures[j] > temperatures[i]:
#                     res[i] = j - i  # Update the number of days to wait
#                     break  # No need to check further

#         return res


