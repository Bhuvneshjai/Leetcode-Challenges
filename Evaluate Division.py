'''
Evaluate Division: You are given an array of variable pairs equations and an array of real numbers values, where
equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that
represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer
for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and
that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
'''
from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1: Build the graph
        graph = defaultdict(dict)

        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value  # Store reciprocal

        # Step 2: Function to perform BFS and find the result of a / b
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0

            queue = deque([(start, 1.0)])  # (current node, current product)
            visited = set()

            while queue:
                node, prod = queue.popleft()

                if node == end:
                    return prod  # Found the target

                visited.add(node)

                for neighbor, value in graph[node].items():
                    if neighbor not in visited:
                        queue.append((neighbor, prod * value))

            return -1.0  # No valid path

        # Step 3: Process all queries
        results = []
        for a, b in queries:
            results.append(bfs(a, b))

        return results


# Test Cases
sol = Solution()

# Example 1
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(sol.calcEquation(equations, values, queries))  # Output: [6.0, 0.5, -1.0, 1.0, -1.0]

# Example 2
equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
values = [1.5, 2.5, 5.0]
queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
print(sol.calcEquation(equations, values, queries))  # Output: [3.75, 0.4, 5.0, 0.2]

# Example 3
equations = [["a", "b"]]
values = [0.5]
queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
print(sol.calcEquation(equations, values, queries))  # Output: [0.5, 2.0, -1.0, -1.0]
