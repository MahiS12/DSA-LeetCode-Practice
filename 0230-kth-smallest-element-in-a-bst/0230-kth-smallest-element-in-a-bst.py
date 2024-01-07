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
        global arr
        arr= []
        
        def inorder(root,arr):
            if not root:
                return
            
            inorder(root.left,arr)
            arr.append(root.val)
            inorder(root.right,arr)
            
        
        inorder(root,arr)
        return arr[k-1]