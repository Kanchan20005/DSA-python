class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        dic1 = {}
        for i in s: 
            wc = s.count(i)
            if wc%2 == 0:
                dic[i] = wc
            else:
                    dic1[i] = wc-1
        val = list(dic.values())
        val1 = list(dic1.values())
        if dic1:
            return sum(val)+sum(val1)+1
        else:
            return sum(val)
        