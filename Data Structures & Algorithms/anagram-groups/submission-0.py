class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 #a-z starting at 0

            for c in s:
                count[ord(c) - ord("a")] += 1 #finding the asci value of the current letter and mapping it to the array index 

            res[tuple(count)].append(s)

        return list(res.values())