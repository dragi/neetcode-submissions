class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 100
        high = 0
        max_profit = 0

        for num in prices:
            if num < low:
                low = num
                continue

            profit = num - low
            if profit > max_profit:
                max_profit = profit

        return max_profit 