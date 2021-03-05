#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        n = len(nums)
        output = []

        for i in range(0, n):
            output.append(prod)
            prod = prod*nums[i]
        
        prod = 1
        for j in range(n-1, -1, -1):
            output[j] = output[j] * prod
            prod = prod * nums[j]
        
        return output

        # Brute Force method
        # total_product=1
        # for num in nums:
        #     total_product *= num
        # new_nums = []
        # if total_product > 0:
        #     for i in nums:
        #         product = total_product // i
        #         new_nums.append(product)    

        # return new_nums
#total_product = 24

# p 1
# n = 4
# i #      0 1 2 3 
# nums #   1 2 3 4 
# output         i
# [1, 1, 2, 6, 24] 
#  
# p # 1
# i #    3  2 1 0
# nums # 24
#output [24, 18, ]
#         
        
        
        # Brute force method but time exceeded since it is O(n^2)

        # renewed_nums = []
        # for i in range(len(nums)):
        #     i_value = nums.pop(i)
        #     prod = 1
        #     for j in nums:
        #         prod = prod * j
        #     renewed_nums.append(prod)
        #     nums.insert(i, i_value)
            
        # return renewed_nums

# 0 1 2 3
# 1 2 3 4
# 24


        
# @lc code=end

