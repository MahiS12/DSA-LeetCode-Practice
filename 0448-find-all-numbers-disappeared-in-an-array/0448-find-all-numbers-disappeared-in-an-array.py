class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        list1 = []
        nums1 = set(nums)
        
        for i in range(1,len(nums)+1):
            
            if i not in nums1:
                list1.append(i)
                
        
        return list1
        