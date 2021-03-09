#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        start , end = 0, len(s) -1

        while start < end:
            while start < end and not s[start].isalnum():
                start+=1
            while start < end and not s[end].isalnum():
                end-=1                
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1

        return True      
        
        
        # Long answer with two seperate loops
        # convert_s = ""

        # if s:
        #     for i in s.lower():
        #         if i.isalnum():
        #             convert_s += i


        # if convert_s:
        #     j , k = 0, len(convert_s) -1

        #     while j <= k:
        #         if convert_s[j] != convert_s[k]:
        #             return False
        #         else:
        #             j+=1
        #             k-=1
            
        # return True
# @lc code=end

