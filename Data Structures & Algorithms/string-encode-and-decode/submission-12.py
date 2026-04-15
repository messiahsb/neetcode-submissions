class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""

        for s in strs:
            out+=str(len(s)) + "#"+s
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        count = ""
        i=0
        while i < (len(s)):
            dec = ""
            if s[i] != "#":
             count += s[i]
            print(s[i])
            if i != 0 and s[i] == "#":
                 if count.isdigit():
                    for x in range(int(count)):
                        i+=1
                        dec+=s[i]
                        
                    count = ""
                    out.append(dec)
            i+=1
        return out
                    
                
