from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]