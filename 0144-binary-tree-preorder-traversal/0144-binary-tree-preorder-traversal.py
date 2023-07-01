# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # l=[]

        # def pre(root):
        #     if not root:
        #         return []
        #     l.append(root)
        #     pre(root.left)
        #     pre(root.right)

        # pre(root)
        # return l

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []