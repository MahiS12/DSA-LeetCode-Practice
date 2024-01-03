class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #O(n+m)
        res = [-1]*len(nums1)
        hashmap ={}
        for i in range(len(nums1)):
            hashmap[nums1[i]]=i
        stack = [] #only storing the elements in nums1
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                x =stack.pop()
                idx = hashmap[x]
                res[idx]= curr
            if curr in hashmap:
                stack.append(curr)
        return res
    
        #O(m.n)
#         res = [-1]*len(nums1)
#         hashmap = {}
#         for i in range(len(nums1)):
#             hashmap[nums1[i]]= i  #we need the index as the value
        
#         for i in range(len(nums2)):
#             if nums2[i] not in hashmap:
#                 continue
            
#             for j in range(i+1,len(nums2)):
#                 if nums2[j] > nums2[i]:
#                     idx = hashmap[nums2[i]]
#                     res[idx]=nums2[j]
#                     break #since we want the first greater element found
        
#         return res
        
        
        
        