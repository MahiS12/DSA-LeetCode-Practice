class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        
        low = 0
        high = len(arr)-1
        
        while low <high:
            
            mid = low + (high-low)//2
            
            
            if arr[mid] > arr[mid+1]:
                high = mid  #checking the left half of the array for greater element
                
            elif arr[mid] < arr[mid+1]:
                low = mid +1 #checking the right half or array for greater
                
        return low
            
            
            
        