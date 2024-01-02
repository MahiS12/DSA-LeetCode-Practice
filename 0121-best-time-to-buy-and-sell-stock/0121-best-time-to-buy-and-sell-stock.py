class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        i = 0
        j =1 
        profit = 0
        
        while j < len(prices):
            curr = prices[j] - prices[i]
            
            if prices[j] > prices[i]:
                profit = max(profit,curr)
            
            else:
                i =j
            j+=1
        
        return profit