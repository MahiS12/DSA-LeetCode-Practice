class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = [0,0]
        
        for n in nums:
            n = abs(n)
            if nums[n-1] < 0:
                res[0] = n
            nums[n-1] = -nums[n-1]
        
        for i, n in enumerate(nums):
            if n >0 and i +1 != res[0]:
                res[1]= i+1
                return res
            
            
#         n = len(nums)
#         actual_sum = n * (n + 1) // 2
#         array_sum = 0
#         unique_sum = 0
#         s = set()

#         for a in nums:
#             array_sum += a

#         for a in nums:
#             s.add(a)

#         for a in s:
#             unique_sum += a

#         missing = actual_sum - unique_sum
#         duplicate = array_sum - unique_sum

#         return [duplicate, missing]

#         n = len(nums)
#         v = [0] * (n + 1)
#         missing, duplicate = 0, 0

#         for num in nums:
#             v[num] += 1

#         for i in range(1, len(v)):
#             if v[i] == 2:
#                 duplicate = i
#             if v[i] == 0:
#                 missing = i

#         return [duplicate, missing]
        
        
        