class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        count = 0
        intervals.sort(key=lambda i:i[0])
        
        prevEnd= intervals[0][1]
        
        for i in intervals[1:]:
            
            if i[0] >= prevEnd:
                prevEnd = i[1]
            else:
                count+=1
                prevEnd = min(i[1],prevEnd) #keep short intervals
        
        return count

#         removals = 0

#         i = 0
#         while i < len(intervals):
#             removed = False
#             j = 0
#             while j < len(intervals):
#                 if i != j and intervals[i][1] > intervals[j][0] and intervals[i][0] < intervals[j][1]:
#                     # Overlap found, remove one of the intervals
#                     removed = True
#                     removals += 1
#                     intervals.pop(j)
#                     break  # Exit the inner loop to restart the process
#                 j += 1

#             if not removed:
#                 i += 1

#         return removals