class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = {}
        for n in nums:
            out[n] = 1 + out.get(n, 0)
        
        res = []
        for n, c in out.items():
            res.append([c, n])    
        res = sorted(res)

        output = []
        while len(output) < k:
            output.append(res.pop()[1])
        return output
