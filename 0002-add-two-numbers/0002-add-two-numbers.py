# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        count=0

        
        dummy = ListNode(0)
        temp= dummy

        while l1 or l2:
            a= l1.val if l1 else 0
            b= l2.val if l2 else 0
            summ= a+b+count

            digit= summ % 10
            count= summ //10

            temp.next = ListNode(digit)
            temp= temp.next
            l1= l1.next if l1 else None
            l2= l2.next if l2 else None
        
        if count:
            temp.next = ListNode(count)
            temp=temp.next
        
            
        return dummy.next



        


        