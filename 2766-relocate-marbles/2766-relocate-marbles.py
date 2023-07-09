class Solution(object):
    def relocateMarbles(self, nums, moveFrom, moveTo):
        """
        :type nums: List[int]
        :type moveFrom: List[int]
        :type moveTo: List[int]
        :rtype: List[int]
        """
        
        s = set(nums)
        
        for f,t in zip(moveFrom,moveTo):
            s.remove(f)
            s.add(t)
        return sorted(s)
        
#         hashmap = defaultdict(int) 
        
#         for num in nums:
#             hashmap[num] += 1
            
#         for i in range(len(moveFrom)):
#             count = hashmap[moveFrom[i]]
#             del hashmap[moveFrom[i]]
#             hashmap[moveTo[i]] += count
                
#         return sorted(hashmap.keys())