class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #collect count of each letter 
        keep_count = {}

        for task in tasks:
            if not task in keep_count.keys():
                keep_count[task] = 0
            keep_count[task] += 1

        #heapify to get the max
        heap_count = []
        for key, val in keep_count.items():
            heap_count.append(-val)
        heapq.heapify(heap_count)

        #calculate the schedule
        dq = deque([])
        time = 0
        while (heap_count or dq):
            if heap_count:
                val = heapq.heappop(heap_count)
                if -val > 1:
                    dq.append((val + 1, time + n ))

            if dq and time >= dq[0][1]:
                val, t = dq.popleft()
                heapq.heappush(heap_count, val)

            time += 1
        return time

        