class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        
        
        q = deque() #indices
        res = []

        
        l = r = 0
        
        while r <len(nums):
            
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            
            q.append(r)
            if l > q[0]:
                q.popleft()
            if (r+1) >=k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res
                
        
       
    
        
        
#         q = deque()
#         res = []
        
#         for i in range(len(nums)):
            
#             #remove elements outside the window
#             while q and q[0] <= i-k:
#                 q.popleft()
                
#             #smaller elements
#             while q and nums[q[-1]] < nums[i]:
#                 q.pop()
#             q.append(i)
            
#             #add the current max element
#             if i >= k-1:
#                 res.append(nums[q[0]])
        
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
            
            
            
            
            
        