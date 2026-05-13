class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = {}
        bucket = [[] for i in range(len(nums)+1)]
        for n in nums:
            out[n] = 1 + out.get(n, 0)
        
        for n,c in out.items():
            bucket[c].append(n)

        res = []
        for x in range(len(bucket)-1, 0, -1):
            for n in bucket[x]:
                res.append(n)
                if len(res) == k:
                    return res
