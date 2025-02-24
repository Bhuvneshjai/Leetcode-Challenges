'''
Maximum Level Sum of a Binary Tree: Given the root of a binary tree, the level of its root is 1, the level of its children
is 2, and so on. Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
'''

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        max_sum = float('-inf')
        max_level = 1
        level = 1

        while queue:
            level_sum = sum(node.val for node in queue)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return max_level


# Helper function to construct a binary tree from a list
def constructTree(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

sol = Solution()

# Example 1
root1 = constructTree([1, 7, 0, 7, -8, None, None])
print(sol.maxLevelSum(root1))  # Output: 2

# Example 2
root2 = constructTree([989, None, 10250, 98693, -89388, None, None, None, -32127])
print(sol.maxLevelSum(root2))  # Output: 2
