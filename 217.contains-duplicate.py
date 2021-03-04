#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Example 1:

# Input: [1,2,3,1]
# Output: true
# Example 2:

# Input: [1,2,3,4]
# Output: false
# Example 3:

# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

# 

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dicto = {}
        for num in nums:
            dicto.setdefault(num, 0)
            dicto[num]+=1
        
        print(dicto)
        for k, v in dicto.items():
            if v > 1:
                return True
        return False

        # One Line solution
        # return len(set(nums)) != len(nums)


# @lc code=end

