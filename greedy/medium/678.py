"""
678. Valid parenthesis string

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*)))"
Output: false

Example 4:
Input: s = "(((((*)))**"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.

"""

class Solution:
    def checkValidString(self, s: str) -> bool:

        stack = []
        wildcard = []

        for i in range(len(s)):
            if s[i] == ')':
                if stack:
                    stack.pop()
                elif wildcard:
                    wildcard.pop()
                else:
                    return False
            elif s[i] == '(':
                stack.append(i)
            else:
                wildcard.append(i)

        #at this point, the stack is only left with the positions of the unmatched '('
        #the below looks to match these to the wildcards that are positioned ahead in the string
        while stack and wildcard:
            i = stack[-1]
            j = wildcard[-1]
            if j > i:
                wildcard.pop()
                stack.pop()
            else:
                return False
        
        return False if stack else True

if __name__ == "__main__":
  tests = [
    "()",
    "(*)",
    "(*)))",
    "(((((*)))**"
  ]

  for test in tests:
    print(Solution().checkValidString(test))