#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [0]
# Output: 0
# Example 4:

# Input: nums = [-1]
# Output: -1
# Example 5:

# Input: nums = [-100000]
# Output: -100000

# Constraints:

# 1 <= nums.length <= 3 * 104
# -105 <= nums[i] <= 105
 
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# @lc code=start
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum = max_sum = nums[0]

        for i in range(1, len(nums)):

            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(curr_sum, max_sum)

        return max_sum


        # Brute force but fails for [-2,1]
        max_sum = nums[0]
        curr_sum = 0
        if len(nums) > 1:
            i = 0
            j = i+1
            
            while i < len(nums) or j < len(nums):
                curr_sum = nums[i] + nums[j]
                if curr_sum > max_sum and i < len(nums) and j == len(nums):
                    max_sum = curr_sum
                    i+=1
                elif curr_sum > max_sum and i < len(nums) and j < len(nums):
                    max_sum = curr_sum
                    j+=1
                else:
                    i+=1
                    j=i+1
        
        return max_sum

# @lc code=end

