class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        
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
                
#         return low
            
            
            
        