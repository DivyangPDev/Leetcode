#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

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

