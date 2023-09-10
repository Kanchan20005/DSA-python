class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        maxProfit = 0
        for i in range(len(prices)):
            if i == 0:
                curstart = prices[0]
                curend = prices[0]
                j = 1
            if curend>=curstart:
                diff = curend-curstart
                if maxProfit < diff:
                    maxProfit = diff
            else:
                curstart = prices[i]

            if i+1 == len(prices):
                break
            curend = prices[i+1]

        return maxProfit