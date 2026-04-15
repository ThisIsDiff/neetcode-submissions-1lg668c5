# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0 # start with 1 b/c starts with a root val comparing a root val which will always count the root node as 1 

        def helperGoodNodes(node, max_val):
            if not node:
                return
            nonlocal res

            if max_val <= node.val:
                res += 1
                max_val = node.val

            helperGoodNodes(node.left, max_val)
            helperGoodNodes(node.right, max_val)
        
        helperGoodNodes(root, root.val)
        return res