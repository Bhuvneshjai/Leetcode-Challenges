'''
Nearest Exit from Entrance in Maze: You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.')
and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol]
denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot
step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell
that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Example 1:
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.

Example 2:
Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.

Example 3:
Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.
'''

from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
        visited = set()
        visited.add(tuple(entrance))

        while queue:
            r, c, steps = queue.popleft()

            # Check if we reached an exit (but not the entrance itself)
            if (r != entrance[0] or c != entrance[1]) and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                return steps  # Return the number of steps to the nearest exit

            # Explore 4 possible directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == "." and (nr, nc) not in visited:
                    queue.append((nr, nc, steps + 1))
                    visited.add((nr, nc))  # Mark as visited to prevent re-visiting

        return -1  # No exit found

sol = Solution()

# Example 1
maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [1,2]
print(sol.nearestExit(maze, entrance))  # Output: 1

# Example 2
maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1,0]
print(sol.nearestExit(maze, entrance))  # Output: 2

# Example 3
maze = [[".","+"]]
entrance = [0,0]
print(sol.nearestExit(maze, entrance))  # Output: -1
