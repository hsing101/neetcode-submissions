import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            num1 = heapq.heappop(heap)
            num2 = heapq.heappop(heap)
            heapq.heappush(heap, -abs(num1-num2))
        return -heapq.heappop(heap)
        