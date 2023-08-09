/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head){
    
    if (head ==NULL)
        return head;
        
    struct ListNode *dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->next = head;
    struct ListNode *prev = dummy;
    
    while (head != NULL && head->next != NULL)
        if (head->val == head->next->val){
            while (head->next !=NULL && head->val==head->next->val){
                                head= head->next;
            }

            head=head->next;
            prev->next = head;
            
        }else{
            
            head= head->next;
            prev=prev->next;
            
        }

    
    
    return dummy->next;
                

}