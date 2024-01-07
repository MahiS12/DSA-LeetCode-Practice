class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key=lambda i:i[0])
        
        res = [intervals[0]]
        
        for i in range(1,len(intervals)):
            
            recentEnd= res[-1][1]
            
            if intervals[i][0] <= recentEnd:
                res[-1][1] = max(recentEnd,intervals[i][1])
            
            else:
                res.append(intervals[i])
        
        return res