class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        res = []
        nums = sorted(nums)

        
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums [i-1]:
                continue
                    
            left = i+1
            right = len(nums)-1

            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                if summ > 0:
                    right -=1
                elif 0 > summ:
                    left +=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    
                    left +=1
                    right -=1
                #checking if its the same value as before to avoid duplicates
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
                    while nums[right] == nums[right+1] and left < right:
                        right -=1
                    
            
        return res
                
            
            
            
    
                        
    
        

        
        
            