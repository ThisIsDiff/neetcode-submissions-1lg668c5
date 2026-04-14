# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def helperLevelOrder(root, level):
            if not root:
                return 

            if len(res) <= level:
                res.append([])

            res[level].append(root.val)
            helperLevelOrder(root.left, level + 1)
            helperLevelOrder(root.right, level + 1)
        

        helperLevelOrder(root, 0)
        return res


"""
check root 
store root.val 


"""