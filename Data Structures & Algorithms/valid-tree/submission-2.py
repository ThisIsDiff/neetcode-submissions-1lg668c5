class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        visited = set()

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        def dfs(parent, current):
            if current in visited:
                return False

            visited.add(current)

            for node in adj[current]:
                if node != parent and not dfs(current,node):
                    return False
            return True
                
        if dfs(None, 0) and len(visited) == n:
            return True
        return False


        