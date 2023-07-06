# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        
        
        dummy = ListNode(0,head)
        curr, leftPrev = head, dummy
        
        #for curr to be at left node
        
        for i in range(left-1):
            leftPrev,curr= curr,curr.next
            
        #reverse left to right
        #curr at left and leftprev at node before curr
        prev = None
        for i in range(right-left+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        
        leftPrev.next.next = curr
        leftPrev.next = prev
        
        return dummy.next
        
        
        
            
            