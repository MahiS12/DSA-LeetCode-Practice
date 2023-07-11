# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_val = float("-inf")
        
        def dfs(root):
            
            nonlocal max_val
            
            if not root:
                return 0
            
            #if we encounter negative value
            left = max (dfs(root.left),0)
            right = max(dfs(root.right),0)
            
            #max without splitting
            
            current = root.val + left + right
            
            max_val = max(max_val,current)
            
            #return the max path without splitting
            
            return (root.val + max(left,right))
        
        
        dfs(root)
        return max_val
        
            
            