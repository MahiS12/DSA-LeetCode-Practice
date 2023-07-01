class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1,-1]
        result[0]= self.binary(nums,target,start= True)
        result[1]= self.binary(nums,target,start= False)

        return result

    def binary(self,nums,target,start):
        low= 0
        high= len(nums)-1
        index=-1

        while low <=high:
            mid= low + (high -low)//2
            if nums[mid] > target:
                high= mid -1
            elif nums[mid]== target:
                index=mid
                if start == True:
                    high= mid-1
                else:
                    low= mid+1
            elif nums[mid] < target:
                low= mid+1
        return index
            
        


        