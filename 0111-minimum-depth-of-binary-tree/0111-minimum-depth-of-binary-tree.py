# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        
        # BFS
        if not root:
            return 0
        
        q = deque([(root, 1)])

        while q:
            cur, depth = q.popleft()
            if not cur.left and not cur.right:
                return depth
            
            else:
                if cur.left:
                    q.append((cur.left, depth+1))
                if cur.right:
                    q.append((cur.right, depth+1))

        
        
        
#         if not root:
#             return 0
        
#         if root.left is None and root.right is None:
#             return 1
        
#         if root.left is None:
#             return 1 + self.minDepth(root.right)
        
#         if root.right is None:
#             return 1 + self.minDepth(root.left)
        
        
#         return 1 + min(self.minDepth(root.left),self.minDepth(root.right))
            
        