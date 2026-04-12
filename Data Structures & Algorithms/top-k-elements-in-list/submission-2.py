import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))  # max heap by frequency

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
