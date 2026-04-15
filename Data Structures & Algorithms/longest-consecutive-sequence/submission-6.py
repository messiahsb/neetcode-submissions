class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        con = set()
        total = 0

        for num in nums:
            con.add(num)


        for num in con:
            count = 1
            while num+count in con:
                count +=1
               
            total = max(total, count)
        return total
            