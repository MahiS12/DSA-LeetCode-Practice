# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        
        
        
        
        #using fast and slow pointer
        
        if not head.next:
            return None
        
        
        slow = fast = head
        prev = None
        
        while fast and fast.next:
            fast= fast.next.next
            prev = slow
            slow = slow.next
            
        
        if prev:
            prev.next = slow.next
        else:
            head = slow.next
            
        return head
            
        
        
        
        
        
        #using count
#         curr = head
#         count = 0
        
#         while curr:
#             count+=1
#             curr = curr.next
            
#         if count <=1:
#             return None
            
#         mid = (count//2)
#         prev = None
#         current = head
#         index = 0
        
#         while current:
#             if index == mid:
#                 prev.next = current.next
#                 break
#             prev = current
#             current= current.next
#             index+=1
        
#         return head

    

                    
                

                
        