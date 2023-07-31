class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        q = deque()
        res = []
        
        l = r = 0
        
        while r < len(nums):
            
            #pop smaller values then current element
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            
            if (r +1) >= k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        
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
            
            
            
            
            
        