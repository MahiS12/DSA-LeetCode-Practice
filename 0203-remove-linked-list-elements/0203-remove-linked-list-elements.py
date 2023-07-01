# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        dummy= ListNode(next=head)
        prev,curr= dummy,head

        while curr:
            temp= curr.next
            if curr.val == val:
                prev.next=temp
            else:
                prev= curr
            curr= curr.next
        return dummy.next