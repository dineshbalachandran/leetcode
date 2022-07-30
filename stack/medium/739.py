"""
Medium

MONOTONICALLY DECREASING STACK example: i.e. a stack maitained in such a way that the 
values in the stack are in decreasing order i.e. the value at the top of the stack is smaller
than the value previous and so on.

Given an array of integers temperatures represents the daily temperatures, return an array 
answer such that answer[i] is the number of days you have to wait after the ith day to get a 
warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 
instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

class Solution:
    def dailyTemperaturesN2(self, temperatures):
        
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)-2, -1, -1):
            if temperatures[i] < temperatures[i+1]:
                answer[i] = 1
            else:
                j = i + 1
                while answer[j] != 0:
                    j += answer[j]
                    if temperatures[i] < temperatures[j]:
                        answer[i] = j - i
                        break
        
        return answer
    
    def dailyTemperatures(self, temperatures):
        
        answer = [0]*len(temperatures)
        
        stack = [] # monotonically decreasing stack
        for (i, t) in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, pos = stack.pop()
                answer[pos] = i - pos
            stack.append((t, i))
            
        return answer

if __name__ == "__main__":
    tests = [
        [73,74,75,71,69,72,76,73],
        [30,40,50,60],
        [30,60,90]
    ]

    for test in tests:
        print(Solution().dailyTemperatures(test))