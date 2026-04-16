# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = 0

        hash_inorder = {} #{} for dictionary
        for i, val in enumerate(inorder):
            hash_inorder[val] = i

        def DFSBuildTree(l, r):
            if l > r: 
                return 
            nonlocal index
            mid = preorder[index]
            index += 1
            root = TreeNode(mid)
            root.left = DFSBuildTree(l,hash_inorder[mid] -1)
            root.right = DFSBuildTree(hash_inorder[mid]+1, r)
            return root


        # DFSBuildTree(0, len(inorder) - 1)
        
        return DFSBuildTree(0, len(inorder) - 1)