class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        list1=[]
        start = nums[0]

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] +1:
                if start == nums[i-1]:
                    list1.append(str(start))
                else:
                    list1.append(str(start) + "->" + str(nums[i-1]))
                start = nums[i]

        if start == nums[-1]:
            list1.append(str(start))
        else:
            list1.append(str(start)+ "->" + str(nums[-1]))

        return list1
        

            
             
            