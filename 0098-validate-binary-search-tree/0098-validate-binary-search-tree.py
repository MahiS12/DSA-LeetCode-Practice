# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def isvalid(node,left,right):
            
            if not node:
                return True
            
            if not(node.val <right and node.val>left):
                return False
            
            leftsub=isvalid(node.left,left,node.val)
            rightsub=isvalid(node.right,node.val,right)
            
            return leftsub and rightsub
        
        
        return isvalid(root,float("-inf"),float("inf"))