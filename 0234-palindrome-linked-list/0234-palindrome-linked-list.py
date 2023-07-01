# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # nums=[]

        # while head:
        #     nums.append(head.val)
        #     head= head.next
        # l,r= 0, len(nums)-1

        # while l<=r:
        #     if nums[l] != nums[r]:
        #         return False
        #     l +=1
        #     r -=1
        # return True


        fast= slow= head

        while fast and fast.next:
            fast= fast.next.next
            slow= slow.next
        
        prev= None
        #reverse the second half
        while slow:
            temp= slow.next
            slow.next = prev
            prev= slow
            slow= temp
        
        fast,slow= head, prev
        while slow:
            if fast.val != slow.val:
                return False
            fast= fast.next
            slow= slow.next
        return True


        



