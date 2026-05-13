class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = {}
        for n in nums:
            out[n] = 1 + out.get(n, 0)
        
        heap = []
        for n,c in out.items():
            heapq.heappush(heap, (c, n))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for x in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
