class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [1]*n
        prefix = 1
        
        for i in range(len(nums)):
            res[i]=prefix
            prefix=prefix*nums[i]
            
        postfix = 1
        for i in range(n-1,-1,-1):
            res[i] = res[i]*postfix
            postfix= postfix*nums[i]
        
        return res
        
        
#         n = len(nums)
#         prefix = [0]*n
#         postfix=[0]*n
        
#         prefix[0]=1
#         postfix[n-1]=1
#         res=[]
        
#         #construct prefix array
#         for i in range(1,n):
#             prefix[i]= prefix[i-1]* nums[i-1]
        
#         #postfix
#         for i in range(n-2,-1,-1):
#             postfix[i] = postfix[i+1]*nums[i+1]
        
#         #every index stores its prefix and postfix
#         for i in range(n):
#             res.append(postfix[i]*prefix[i])
        
#         return res
        
        

#         n = len(nums)
#         answer = []

#         for i in range(n):
#             product = 1
#             for j in range(n):
#                 if i != j:
#                     product *= nums[j]
#             answer.append(product)

#         return answer
