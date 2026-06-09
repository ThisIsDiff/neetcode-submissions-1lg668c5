"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution: 
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        hmap = {}
        root = None
        def dfs(node):
            nonlocal root
            nonlocal hmap
            if node.val in hmap.keys():
                return


            new_node = Node(node.val)
            hmap[node.val] = new_node
            
            if root is None:
                root = new_node

            for neighbor in node.neighbors:
                dfs(neighbor)

            for neighbor in node.neighbors:
                clone = hmap[neighbor.val]
                new_node.neighbors.append(clone)

        dfs(node)
        return root

            

