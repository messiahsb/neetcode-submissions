class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += str(len(s)) +"#" + s
        return out

    def decode(self, s: str) -> List[str]:
        out = [] 
        c = 0
        while c < len(s):
            j = c
            while s[j] != '#':
                j+=1
            length = int(s[c:j])
            c = j+1
            j = c + length
            out.append(s[c:j])
            c=j   
        return out
