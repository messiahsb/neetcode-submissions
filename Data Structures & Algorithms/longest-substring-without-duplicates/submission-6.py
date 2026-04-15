class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        length = 0
        sub = set()

        for curChar in range(len(s)):
            while s[curChar] in sub:
                sub.remove(s[start])
                start+=1
            sub.add(s[curChar])
            length = max(length, len(sub))
        return length