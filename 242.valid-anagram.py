#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram

# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Short and concise
        s_dict, t_dict = {}, {}
        for item in s:
            s_dict[item] = s_dict.get(item, 0)+1
        for item in t:
            t_dict[item] = t_dict.get(item, 0)+1

        return s_dict == t_dict
        
        
        #Long answer 
        # if len(s) != len(t):
        #     return False
        # s_dict = {}
        # t_dict = {}
        # for ch in s:
        #     if ch not in s_dict:
        #         s_dict[ch] = 1
        #     else:
        #         s_dict[ch] += 1
        
        # for c in t:
        #     if c not in t_dict:
        #         t_dict[c] = 1
        #     else:
        #         t_dict[c] += 1
            
        # return s_dict == t_dict   
        

        
# @lc code=end

