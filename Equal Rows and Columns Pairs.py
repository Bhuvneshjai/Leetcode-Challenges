'''
Equal Row and Column Pairs: Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that
row ri and column cj are equal. A row and column pair is considered equal if they contain the same elements in the
same order (i.e., an equal array).

Example 1:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
'''

from collections import Counter
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        row_counts = Counter(tuple(row) for row in grid)
        col_counts = Counter(tuple(grid[i][j] for i in range(n)) for j in range(n))
        return sum(row_counts[row] * col_counts[row] for row in row_counts if row in col_counts)

sol = Solution()
result = sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]])
print(result)