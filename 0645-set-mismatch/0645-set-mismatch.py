class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        actual_sum = n * (n + 1) // 2
        array_sum = 0
        unique_sum = 0
        s = set()

        for a in nums:
            array_sum += a

        for a in nums:
            s.add(a)

        for a in s:
            unique_sum += a

        missing = actual_sum - unique_sum
        duplicate = array_sum - unique_sum

        return [duplicate, missing]

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
        
        
        