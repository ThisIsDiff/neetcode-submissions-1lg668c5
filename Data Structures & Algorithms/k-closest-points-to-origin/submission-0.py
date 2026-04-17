class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2))

        def cal_distance(x, y):
            return math.sqrt(x**2 + y**2)

        closest_ls = []

        for x, y in points:
            dist = cal_distance(x,y)
            closest_ls.append((dist, [x,y]))

        heapq.heapify(closest_ls)
        print(closest_ls)
        res = []

        for _ in range(k):
            dist, point = heapq.heappop(closest_ls)
            res.append(point)
        return res