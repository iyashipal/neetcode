class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0
        for x in prices:
            if x < min:
                min = x
            if x < min: 
                sell = True
                max = x
            if profit < x - min:
                profit = x - min
            

        return profit
            