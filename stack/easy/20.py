"""
Easy
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(])"
Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for c in s:           
            if (stack and 
                ((c == '}' and stack[-1] == '{') or 
                (c == ']' and stack[-1] == '[') or
                (c == ')' and stack[-1] == '('))
                ):
                stack.pop()
            else:
                stack.append(c)
            
        return False if stack else True

if __name__ == "__main__":
    tests = [
        "()",
        "()[]{}",
        "(])"
    ]

    for test in tests:
        print(Solution().isValid(test))