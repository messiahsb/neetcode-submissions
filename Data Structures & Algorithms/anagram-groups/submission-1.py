class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for s in strs:
            bucket = [0]*26
            for x in s:
                bucket[ord(x) - ord('a')] += 1
            ana[tuple(bucket)].append(s)

        return list(ana.values())