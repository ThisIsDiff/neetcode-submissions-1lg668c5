class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)] 
        visited = set()
        print(adj)

        for u, v, t in times:
            adj[u].append((v,t))

        hq = [(0,k)]
        heapq.heapify(hq)
        res_time = 0
        while hq:
            time, node = heapq.heappop(hq)
            if node in visited:
                continue
            visited.add(node)
            res_time = time
            for vn, tn in adj[node]:
                if vn not in visited:
                    heapq.heappush(hq,(time+tn, vn))
        if len(visited) != n:
            return -1
        return res_time
