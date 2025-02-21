'''
Longest ZigZag Path in a Binary Tree: You are given the root of a binary tree. A ZigZag path for a binary tree is
defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:
Input: root = [1]
Output: 0
'''

from typing import Optional, List
from collections import deque, defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLeafValues(self, root: Optional[TreeNode]) -> List[int]:
        leaf_values = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            if not node.left and not node.right:
                leaf_values.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return leaf_values

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeafValues(root1) == self.getLeafValues(root2)

    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            good = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            return good + dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(root, root.val)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        def dfs(node: Optional[TreeNode], curr_sum: int) -> int:
            if not node:
                return 0

            curr_sum += node.val
            count = prefix_sum[curr_sum - targetSum]
            prefix_sum[curr_sum] += 1

            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            prefix_sum[curr_sum] -= 1
            return count

        return dfs(root, 0)

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0

        def dfs(node: Optional[TreeNode], direction: int, length: int):
            if not node:
                return
            self.max_length = max(self.max_length, length)
            if direction == 0:
                dfs(node.left, 1, length + 1)
                dfs(node.right, 0, 1)
            else:
                dfs(node.right, 0, length + 1)
                dfs(node.left, 1, 1)

        dfs(root, 0, 0)
        dfs(root, 1, 0)
        return self.max_length


# Function to construct a binary tree from a list
def constructTree(values: List[Optional[int]]) -> Optional[TreeNode]:
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

# Create a Solution instance
sol = Solution()

# Example input
arr = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]

# Construct the tree
root = constructTree(arr)

# Get the longest ZigZag path
print(sol.longestZigZag(root))  # Output: 3