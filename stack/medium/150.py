"""
Medium
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression 
would always evaluate to a result, and there will not be any division by zero operation.

 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

class Solution:
    def evalRPN(self, tokens) -> int:
        op = {
            '+': (lambda a,b: a+b),
            '-': (lambda a,b: a-b),
            '*': (lambda a,b: a*b),
            '/': (lambda a,b: int(a/b))
            }
        
        stack = []
        for t in tokens:
            if t in op:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(op[t](a, b))                
            else:
                stack.append(t)
        
        return stack[-1]
    
if __name__ == "__main__":
    tests = [
        ["2","1","+","3","*"],
        ["4","13","5","/","+"],
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    ]

    for test in tests:
        print(Solution().evalRPN(test))