# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        high = max(p.val, q.val)
        low = min(p.val, q.val)
        while (root):
            if root.val < low:
                root = root.right
            elif root.val > high:
                root = root.left
            elif low < root.val < high:
                return root
            else:
                return root