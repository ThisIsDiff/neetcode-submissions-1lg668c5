# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helperLCA(self, root, low, high):
        if root.val == low or root.val == high:
            return root

        if low <= root.val <= high:
            return root
        
        if root.val > high:
            root = root.left
        elif root.val < low:
            root = root.right

        return self.helperLCA(root,low, high)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        high = max(p.val,q.val)
        low = min(p.val,q.val)

        return self.helperLCA(root, low, high)
