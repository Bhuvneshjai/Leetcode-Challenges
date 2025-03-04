'''
Rotting Oranges: You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Step 1: Find all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, minutes)
                elif grid[r][c] == 1:
                    fresh_count += 1

        # If there are no fresh oranges, return 0
        if fresh_count == 0:
            return 0

        # Step 2: BFS Traversal
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        minutes_passed = 0

        while queue:
            r, c, minutes = queue.popleft()
            minutes_passed = max(minutes_passed, minutes)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Rotten the fresh orange
                    fresh_count -= 1
                    queue.append((nr, nc, minutes + 1))

        # Step 3: Check if all fresh oranges are rotten
        return minutes_passed if fresh_count == 0 else -1

sol = Solution()
grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]

print(sol.orangesRotting(grid))