#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
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

