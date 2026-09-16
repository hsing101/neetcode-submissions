class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for task in tasks:
            freq[task] -= 1
        time = 0
        heap = list(freq.values())
        heapq.heapify(heap)
        queue = deque()
        while heap or queue:
            time += 1
            if heap:
                val = heapq.heappop(heap) + 1
                if val:
                    queue.append((val, n + time))
            else:
                time = queue[0][1]
            if queue and time == queue[0][1]:
                new_val, new_time = queue.popleft()
                heapq.heappush(heap, new_val)
        return time


        

            


