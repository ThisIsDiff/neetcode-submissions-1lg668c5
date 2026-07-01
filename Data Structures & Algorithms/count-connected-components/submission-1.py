class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = [[] for _ in range(n)]

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        def dfs(parent, current):
            if current in visited:
                return 
            visited.add(current)
            for node in adj[current]:
                if parent!= node:
                     dfs(current, node)
            return

        result = 0
        for i in range(n):
            if i not in visited:
                dfs(None, i)
                result += 1
        return result