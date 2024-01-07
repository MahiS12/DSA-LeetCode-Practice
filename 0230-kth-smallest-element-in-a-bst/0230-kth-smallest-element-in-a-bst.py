# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        
        def inorder(root,count,ans):
            if not root:
                return
        
            inorder(root.left,count,ans)
            count[0]-=1
            if count[0]==0:
                ans[0] = root.val
                return
            inorder(root.right,count,ans)
        
        ans = [0]
        count=[k]
        inorder(root,count,ans)
        return ans[0]
        
        
#         stack = []
#         curr = root

#         while stack or curr:
#             while curr:
#                 stack.append(curr)
#                 curr = curr.left
#             curr = stack.pop()
#             k -= 1
#             if k == 0:
#                 return curr.val
#             curr = curr.right
        
    
        
#         global arr
#         arr= []
        
#         def inorder(root,arr):
#             if not root:
#                 return
            
#             inorder(root.left,arr)
#             arr.append(root.val)
#             inorder(root.right,arr)
            
        
#         inorder(root,arr)
#         return arr[k-1]