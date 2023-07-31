class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        q = deque()
        res = []
        
        for i in range(len(nums)):
            
            #remove elements outside the window
            while q and q[0] <= i-k:
                q.popleft()
                
            #smaller elements
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
    
            
            q.append(i)
            
            #add the current max element
            if i >= k-1:
                res.append(nums[q[0]])
        
        return res
        
        
        
#         res = []
#         for i in range(len(nums) - k + 1):
#             current_max = float(-inf)
#             for j in range(i, i + k):
#                 current_max = max(nums[j], current_max)
#             res.append(current_max)
        
#         return res
        
        
        #TLE
#         arr = []
#         if k == len(nums):
#             arr.append(max(nums))
#             return arr
        
#         j = k-1
        
#         i = 0
        
#         while j < len(nums):
            
#             arr.append(max(nums[i:j+1]))
#             i+=1
#             j+=1
        
#         return arr
            
            
            
            
            
        