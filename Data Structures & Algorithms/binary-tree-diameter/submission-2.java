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

    int res = 0;

    public int dfs(TreeNode node) {
        
        if (node == null) {
            return 0;
        }

        int left = dfs(node.left);
        int right = dfs(node.right);
        res = Math.max(res, left + right);

        return 1 + Math.max(dfs(node.left), dfs(node.right));
    }

    public int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        return res;
    }
}
