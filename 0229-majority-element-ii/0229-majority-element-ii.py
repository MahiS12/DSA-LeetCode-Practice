class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # O(n) time and O(1) space
        
        ans1 = ans2 = -10**10
        c1 = c2 = 0
        n = len(nums)
        
        for i in range(len(nums)):
            
            if nums[i] == ans1:
                c1+=1
            elif nums[i] == ans2:
                c2+=1
            elif c1 == 0:
                ans1 = nums[i]
                c1=1
            elif c2 == 0 :
                ans2 = nums[i]
                c2=1
            else:
                c1-=1
                c2-=1
            
        # we might have only 1 majority element
        
        
        count1 = 0
        count2 = 0
        a = []
        for i in nums:
            if ans1 == i:
                count1+=1
            
            if ans2 == i:
                count2+=1
                
        
        if count1 > n//3:
            a.append(ans1)
            
        if count2 > n//3:
            a.append(ans2)
            
        return a
        
            
        

        
        