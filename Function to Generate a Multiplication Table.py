'''
Function to Generate a Multiplication Table
'''

class Solution:
    def table(self, num: int) -> list:
        return [num * i for i in range(1,11)]

    def table_lambda(self, num: int) -> list:
        table = lambda num: [num*i for i in range(1,11)]
        return table(num)

sol = Solution()
result = sol.table(5)
print(result)

table = lambda num: [num * i for i in range(1,11)]
print(table(5))

result1 = sol.table_lambda(2)
print(result1)