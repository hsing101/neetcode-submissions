class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            # 2. If the heap is full, only push if num is larger than the min
            elif num > heap[0]:
                heapq.heappush(heap, num)
                heapq.heappop(heap) # Remove the old minimum to keep size k
        return heap[0]



        