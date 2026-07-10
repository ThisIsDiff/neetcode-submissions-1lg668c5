class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhDistance_lambda = lambda point1, point2: abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        visited = set()
        pq = [(0,tuple(points[0]))]
        heapq.heapify(pq)
        result = 0
        while pq:
            dis, point = heapq.heappop(pq)
            if point in visited:
                continue

            visited.add(point)
            result += dis

            for p in points:
                p = tuple(p)
                if p not in visited:
                    distance = manhDistance_lambda(point, p)
                    
                    heapq.heappush(pq, (distance, p))

        return result

