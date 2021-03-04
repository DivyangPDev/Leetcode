#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = -sys.maxsize
        for j in range(1, len(prices)):
            if prices[j] - lowest > max_profit:
                max_profit = prices[j] - lowest

            if prices[j] < lowest:
                lowest = prices[j]
        if max_profit > 0:
            return max_profit
        else:
            return 0


            
# 7 1 5 3 6 4
#   l       p 

# 1 - 6 = -5 > -inf? -> max_profit = -5
# 5 - 1 = 4 > -5 ? -> max_profit = 4
# 3 - 1 = 2 > 4 ? -> max_profit = 4
# 6 - 1 = 5 > 4 ?-> max_profit = 5
# 4 - 1 = 3 > 5 ? -> max_profit = 5

# @lc code=end

