# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = temp = ListNode(0)
        while l1 != None and l2 != None: #1

            if l1.val < l2.val: #2
                temp.next = l1 #3
                l1 = l1.next #4
            else: 
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2  #5
        return dummy.next #6

        # newHead = dummyHead = ListNode()
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         dummyHead.next = list1
        #         list1 = list1.next
        #     else:
        #         dummyHead.next = list2
        #         list2 = list2.next
        #     dummyHead = dummyHead.next
        
        # if list1:
        #     dummyHead.next = list1
        # if list2:
        #     dummyHead.next = list2
        # return newHead.next