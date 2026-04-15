# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def helperKth(node):
            if not node:
                return

            helperKth(node.left)
            res.append(node.val)
            helperKth(node.right)

        helperKth(root)
        return res[k-1]
        