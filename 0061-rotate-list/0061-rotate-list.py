# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        
        if not head:
            return head
        
        curr = head
        count = 1
        
        while curr.next:
            curr = curr.next
            count+=1
            
        k = k % count
        
        if k ==0:
            return head
        
        left = head
        
        for i in range(count-k-1):
            left = left.next
            
        newhead = left.next
        left.next = None
        curr.next = head
        return newhead
            
        
        
        
            
            
            
        
        
        
        