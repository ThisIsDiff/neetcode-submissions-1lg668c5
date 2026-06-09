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
        def dfs(node):
            if node.val in hmap.keys():
                return hmap[node.val]

            new_node = Node(node.val)
            hmap[node.val] = new_node

            for neighbor in node.neighbors:
                clone = dfs(neighbor)
                new_node.neighbors.append(clone)

            return new_node

        return dfs(node)

            

