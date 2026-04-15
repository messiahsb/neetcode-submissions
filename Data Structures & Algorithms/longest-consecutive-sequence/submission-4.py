class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        ret = 0

        for num in nums:
            i=0
            if num-1 not in numset:
                while num+i in numset:
                    i+=1
                ret = max(i, ret)
        return ret
