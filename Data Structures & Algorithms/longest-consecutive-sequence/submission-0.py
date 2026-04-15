class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set()
        ret = 0
        for num in nums:
            numset.add(num)

        for num in nums:
            i=0
            if num-1 in numset:
                continue
            else:
                while num+i in numset:
                    i+=1
                    if ret < i:
                        ret = i
        return ret
