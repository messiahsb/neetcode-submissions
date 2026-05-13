class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)
        for strng in strs:
            bucket = [0]*26
            for c in strng:
                bucket[ord('z') - ord(c)] += 1
            out[tuple(bucket)].append(strng)
        
        return list(out.values())