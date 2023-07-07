# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return None
        
        dummy = ListNode(0,head)
        prev = dummy
        
        while head and head.next:
            if head.val == head.next.val:
                while head.next and head.val == head.next.val: #while duplicates are found
                    head = head.next
                head = head.next
                prev.next = head
            else:
                prev = prev.next
                head= head.next
        return dummy.next
    

        
        