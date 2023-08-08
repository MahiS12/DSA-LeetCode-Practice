/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* insertGreatestCommonDivisors(struct ListNode* head){
    
    
    if (head-> next == NULL){
        return head;
    }
    
    int gcd(int a,int b){
        
        while (b){
            
            int r = a;
            a = b;
            b = r%b;
                
        }
        return a;
        
    }


    struct ListNode *h = head;
    while(head->next != NULL) {
            int r = gcd(head->val, head->next->val);
            struct ListNode* newnode = (struct ListNode*)malloc(sizeof(struct ListNode));
            newnode->val = r;
            struct ListNode *temp = head->next;
            head->next = newnode;
            newnode->next = temp;
            head = newnode->next;
        }
    return h;

}