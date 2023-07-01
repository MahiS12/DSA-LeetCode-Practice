class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = len(nums)
        # nums.sort()
        # if x > 1:
        #     for i in range(x - 1):
        #         if nums[i + 1] == nums[i] + 1:
        #             continue
        #         else:
        #             return nums[i] + 1
        # # Return the missing number if the loop completes
        # return nums[-1] +1

        return (x* (x+1)) //2 - sum(nums)
