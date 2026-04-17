class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for val in stones:
            heapq.heappush(max_heap, -val)

        while (len(max_heap) > 1):
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            res = x - y

            if res != 0:
                heapq.heappush(max_heap, -abs(res))

        return -max_heap[0] if max_heap else 0
