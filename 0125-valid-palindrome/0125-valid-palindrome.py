class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = s.lower()
        t = ''
        for i in r:
            if i.isalnum():
                t = t+i
        return t[::-1] == t
