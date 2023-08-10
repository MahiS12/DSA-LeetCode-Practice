/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int minDepth(TreeNode root) {
        
        if (root ==null){
            return 0;
        }
        
        int x;
        int y;
        
        x = minDepth(root.left);
        y = minDepth(root.right);
        
        if(root.left==null){
            return y+1;
        }
        
        else if(root.right==null){
            return x+1;
        }
        
        return 1 + Math.min(x,y);
        
        
    }
}