class Solution(object):
    def relocateMarbles(self, nums, moveFrom, moveTo):
        """
        :type nums: List[int]
        :type moveFrom: List[int]
        :type moveTo: List[int]
        :rtype: List[int]
        """
        
        marbles = defaultdict(int)  # Dictionary to store the count of marbles

        # Count the marbles and store their count in the dictionary
        for num in nums:
            marbles[num] += 1
            
        for i in range(len(moveFrom)):
            count = marbles[moveFrom[i]]
            del marbles[moveFrom[i]]
            marbles[moveTo[i]] += count
                
        return sorted(marbles.keys())