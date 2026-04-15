class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for word in strs:
            out += str(len(word))+"#" + word
        return out
   
    def decode(self, s: str) -> List[str]:
        word = ""
        delim = ""
        out = []
      #  print(s)
        c = 0
        while c < (len(s)):
            
            delim += s[c]
            if s[c] == "#":
                delim = delim[:-1]
                for i in range(1, int(delim)+1, 1):
                   # print(s[c+i])
                    
                    word += s[c+i]
                out.append(word)
                c+=int(delim)
                print(c)
                word = ""
                delim = ""
            c+=1
                
        return out        