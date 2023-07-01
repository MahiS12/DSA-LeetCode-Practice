# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # count= 0
        # curr= head
        # while curr:
        #     count+=1 
        #     curr= curr.next
        # if count == n:
        #     return head.next
        # curr1= head
        # temp= None
        # prev= None
        # # dummy= ListNode(next=head)
        # while count !=0:
        #     temp = curr1.next
        #     if count == n:
        #         prev.next = temp
        #         return head
        #     else:
        #         prev= curr1
        #         count-=1
        #     curr1= curr1.next

        dummy= ListNode(next=head)
        left =  dummy
        right = head

        while n >0 and right:
            right= right.next
            n -=1
        
        while right:
            left= left.next
            right= right.next
        
        left.next= left.next.next
        return dummy.next






                




        

        



