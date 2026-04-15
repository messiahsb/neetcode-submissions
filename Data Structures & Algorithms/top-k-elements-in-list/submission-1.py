class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num,0)

        out = []

        for key, value in count.items():
            bucket[value].append(key) 
        
        for amounts in range(len(bucket) - 1, 0, -1):
            for numbers in bucket[amounts]:
                if len(out) == k:
                    return out
                out.append(numbers)
        return out        
