'''
Count Good Nodes in Binary Tree: Given a binary tree root, a node X in the tree is named good if in the path from root to
X there are no nodes with a value greater than X. Return the number of good nodes in the binary tree.

Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
'''

from typing import Optional, List
from collections import deque


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

# Example input
arr = [3,1,4,3,None,1,5]

# Construct the tree
root = constructTree(arr)

# Create a Solution instance
sol = Solution()

# Get the count of good nodes
print(sol.goodNodes(root))  # Output: 4


