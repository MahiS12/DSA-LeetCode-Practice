# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head.next:
            return head
        
        def gcd(n1,n2):
            
            while n2:
                n1,n2 = n2, n1 % n2
            return abs(n1)
        
        
        curr = head
        temp = head.next
        
        while temp:
            
            new = ListNode(gcd(curr.val,temp.val))
            
            curr.next = new
            new.next = temp
            curr= temp
            temp = temp.next
        
        return head
            
            
            
            
            
            
            
            
        