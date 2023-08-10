# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        
        q = []
        q.append(root)
        
        ans = None
        
        while len(q) >0:
            
            node = q.pop(0)
            ans = node.val
            
            if node.right is not None:
                q.append(node.right)
            
            if node.left is not None:
                q.append(node.left)

        
        return ans
        