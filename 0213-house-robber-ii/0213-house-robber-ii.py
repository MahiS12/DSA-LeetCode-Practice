class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        def robber(a):
            if not a:
                return 0
            if len(a)==1:
                return a[0]
            
            dp = [0]*len(a)
            dp[0]=a[0] #prev
            
            for i in range(1,len(a)):
                taken = a[i]
                
                if i>1:
                    taken= taken + dp[i-2]
                nottaken= 0 + dp[i-1]
                dp[i]= max(taken,nottaken)
                
            return dp[i]
        
        if len(nums) ==1:
            return nums[0]
        
        ans1 = robber(nums[1:]) #starting from first index to include the last
        ans2= robber(nums[:-1]) #excluding the last element
        return max(ans1,ans2)