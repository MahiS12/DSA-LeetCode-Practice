# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow= head
        fast = head

        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        return slow

        # length= count= 0
        # temp= head
        # while temp:
        #     length+=1
        #     temp= temp.next
        # if length==1:
        #     return head
        
        # mid= length//2

        # while head:
        #     count+=1
        #     head=head.next
        #     if count==mid:
        #         return head
        # return None
