class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        #code 1
#         l =1
#         r= len(arr)-2
        
#         while l <=r:
#             mid = l +(r-l)//2
#             if arr[mid-1] <arr[mid] <arr[mid+1]:
#                 l = mid+1
#             elif arr[mid-1] > arr[mid] >arr[mid+1]:
#                 r = mid-1
#             else:
#                 return mid

        
#         #code 2
        
        low = 0
        high = len(arr)-1
        
        while low <=high:
            
            mid = low + (high-low)//2
            if arr[mid]>=arr[mid-1] and arr[mid]>=arr[mid+1]:
                return mid
            
            if arr[mid] > arr[mid+1]: #decreasing part of array, look in left
                high = mid-1  #checking the left half of the array for greater element
                
            elif arr[mid] < arr[mid+1]: #look in right
                low = mid +1 #checking the right half or array for greater
                
        return low


            
            
        