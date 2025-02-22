'''
Function to Generate a Multiplication Table
'''

class Solution:
    def table(self, num: int) -> list:
        return [num * i for i in range(1,11)]

sol = Solution()
result = sol.table(5)
print(result)

table = lambda num: [num * i for i in range(1,11)]
print(table(5))