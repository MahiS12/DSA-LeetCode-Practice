class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
#         i = 0
#         j =1
#         profit = 0
        
#         while j < len(prices):
#             curr = prices[j] - prices[i]
            
#             if prices[j] > prices[i]:
#                 profit = max(profit,curr)
#             else:
#                 i +=1
#             j+=1
#         return profit
    

        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
        