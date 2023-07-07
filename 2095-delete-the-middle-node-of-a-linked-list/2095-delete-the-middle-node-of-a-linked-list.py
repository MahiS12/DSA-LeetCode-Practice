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
        
        
        curr = head
        count = 0
        # dummy = ListNode(0,head)
    
        
        while curr:
            count+=1
            curr = curr.next
            
        if count <=1:
            return None
            
        mid = (count//2)
        prev = None
        current = head
        index = 0
        
        while current:
            if index == mid:
                prev.next = current.next
                break
            prev = current
            current= current.next
            index+=1
        
        return head

                    
                

                
        