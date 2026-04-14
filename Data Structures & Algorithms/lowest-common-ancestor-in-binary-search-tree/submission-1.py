# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursiveCommAnc( self, root: TreeNode, high: TreeNode, low: TreeNode) -> TreeNode:
        if not root:
            return
        elif high.val > root.val and root.val > low.val:
            return root
        elif (high.val > root.val and low.val > root.val):
            return self.recursiveCommAnc(root.right, high, low)
        elif (high.val == root.val):
            return high
        elif (low.val == root.val):
            return low
        else:
            return self.recursiveCommAnc(root.left, high, low)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if (p.val > q.val):
            high = p
            low = q
        else :
            high = q
            low = p




        res = self.recursiveCommAnc(root, high, low)

        return res

