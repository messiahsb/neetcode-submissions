class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = len(s)-1
        for c in range(math.ceil(len(s)/2)):
           # print(f"c: {s[c]}")
           #print(f"c: {s[i]}")
            if s[c].isalnum() == False : 
                continue
            while s[i].isalnum() == False: 
                i-=1

            if  s[c] != s[i]:
                return False
            i-=1   

        return True