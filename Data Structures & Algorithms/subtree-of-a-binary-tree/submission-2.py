# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSametree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and q) and p.val == q.val:
            return self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right)      
        elif (not p and not q):
            return True
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root: 
            if root.val == subRoot.val and self.isSametree(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return False