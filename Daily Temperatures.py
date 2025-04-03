'''
Daily Temperatures: Given an array of integers temperatures represents the daily temperatures, return an array answer
such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is
no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
'''

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n  # Initialize answer array with zeros
        stack = []  # Stack to keep indices

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index  # Calculate wait days
            stack.append(i)  # Push current index onto the stack

        return answer

sol = Solution()
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
