"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []
        
        res = []
        q = deque()
        q.append(root)
        
        while q:
            level = []
            
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                # print(node.val,end=" ")
                
                for i in node.children:
                    q.append(i)
                
            res.append(level)
        
        return res
        