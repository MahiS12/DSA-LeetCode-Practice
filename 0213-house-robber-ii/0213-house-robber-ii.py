class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        def robber(a):
            
            prev2= 0
            prev = a[0]
            
            for i in range(1,len(a)):
                taken = a[i]
                if i>1:
                    taken= a[i]+prev2
                nottaken= prev
                curr= max(taken,nottaken)
                prev2=prev
                prev=curr
            return prev
        
        if len(nums) <=1:
            return nums[0]
        
        ans1 = robber(nums[1:]) #starting from first index to include the last
        ans2= robber(nums[:-1]) #excluding the last element
        return max(ans1,ans2)