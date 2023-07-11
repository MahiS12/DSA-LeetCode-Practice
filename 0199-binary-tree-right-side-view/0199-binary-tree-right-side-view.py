# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        #dfs
        
        def dfs(root,depth):
            if not root:
                return 
            nonlocal ans
            
            if depth == len(ans): #if we are visiting a level first time,add the node
                ans.append(root.val)
            
            dfs(root.right,depth+1)
            dfs(root.left, depth+1)
            
        dfs(root,0)
        return ans
        
#         #bfs
#         if not root:
#             return []
        
#         res = []
        
#         q = deque([root])
        
#         while q:
#             qlen = len(q)
            
#             for _ in range(qlen):
                
#                 node = q.popleft()
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
                    
#             res.append(node.val)
#         return res
        