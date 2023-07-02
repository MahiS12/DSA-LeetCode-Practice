class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        j =1
        profit = 0
        
        while j < len(prices):
            curr = prices[j] - prices[i]
            if prices[j] > prices[i]:
                profit = max(profit,curr)
            else:
                i = j
            j+=1
        return profit
    

        