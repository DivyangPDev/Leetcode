#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicto = {}
        for i in range(len(nums)):
            diff= target - nums[i] # 9-2
            if diff not in dicto:
                dicto[nums[i]] = i
            else:
                return dicto[diff], i 

# @lc code=end