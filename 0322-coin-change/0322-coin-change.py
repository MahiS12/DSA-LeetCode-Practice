class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float("inf")] *(amount+1)
        dp[0]=0
        
        for i in range(1,amount+1):
            for c in coins:
                if i-c >=0:
                    
                    dp[i]= min(dp[i],1+dp[i-c]) #dp[7] = 1+dp[3] if coin 4 is selected
            
        if dp[amount] != float("inf"):
            return dp[amount]
        else:
            return -1