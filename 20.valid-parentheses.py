#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # par_dict = {'}':'{', ']':'[',')':'('}

        # for par in s:
        #     if par in par_dict.values():
        #         stack.append(par)
        #     elif  par in par_dict.keys():
        #         if stack == [] or par_dict[par] != stack.pop():
        #             return False
        #     else:
        #         return False
        # return stack == []

        # Long answer
        stack = []
        for par in s:
            if par in ['(', '[', '{']:
                stack.append(par)
            elif par == ')':
                if stack == [] or stack.pop() != '(':
                        return False
            elif par == '}':
                if stack == [] or stack.pop() != '{':
                        return False
            elif par == ']':
                if stack == [] or stack.pop() != '[':
                        return False
        
        return stack == []
        
        
        

# @lc code=end

