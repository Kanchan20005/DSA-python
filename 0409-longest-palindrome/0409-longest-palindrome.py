class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        hasodd = False
        for i in s: 
            if i in dic:
                continue
            wc = s.count(i)
            if wc%2 == 0:
                dic[i] = wc
            else:
                if not hasodd:
                    dic[i] = wc
                    hasodd = True
                else:
                    dic[i] = wc-1
        val = list(dic.values())
        return sum(val)
        