/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int minDepth(struct TreeNode* root){
    
    if (root == NULL){
        return 0;
    }
    
    int x,y;
    
    x = minDepth(root->left);
    y = minDepth(root->right);
    
    // if ((x==0) ^ (y==0))
    //     return (x>y?x:y)+1;
    
    if (root->left == NULL)
        return y+1;
    
    else if (root->right ==NULL)
        return x+1;
    
    return 1 + fmin(x,y);
    
    
    
    
    

}