class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        right = len(s)-1
        for left in range(math.ceil(len(s)/2)):
            if not s[left].isalnum():
                continue
            while not s[right].isalnum():
                right-=1
            if s[left] != s[right]:
                return False
            right -=1

        return True