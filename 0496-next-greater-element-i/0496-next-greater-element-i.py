class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        res = [-1]*len(nums1)
        hashmap = {}
        for i in range(len(nums1)):
            hashmap[nums1[i]]= i
        
        for i in range(len(nums2)):
            if nums2[i] not in hashmap:
                continue
            
            for j in range(i+1,len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = hashmap[nums2[i]]
                    res[idx]=nums2[j]
                    break #since we want the first greater element found
        
        return res
        
        
        
        