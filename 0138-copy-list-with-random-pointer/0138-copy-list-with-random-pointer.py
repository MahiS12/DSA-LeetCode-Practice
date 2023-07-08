"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

    # Step 1: Create copies of nodes
        current = head
        while current:
            new_node = Node(current.val, current.random)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

    # Step 2: Set random pointers
        current = head
        while current:
            if current.random is not None:
                current.next.random = current.random.next
            current = current.next.next

    # Step 3: Split the lists
        current = head
        new_head = head.next
        new_current = new_head
        while current:
            current.next = new_current.next
            current = current.next
            if new_current.next:
                new_current.next = new_current.next.next
            new_current = new_current.next

        return new_head
        
        
#         copyMap = {None:None}
        
#         curr = head
        
#         while curr:
#             copy = Node(curr.val)
#             copyMap[curr] = copy
#             curr= curr.next
            
        
#         curr = head
        
#         while curr:
#             copy = copyMap[curr]
#             copy.next = copyMap[curr.next]
#             copy.random = copyMap[curr.random]
#             curr= curr.next
        
#         return copyMap[head]