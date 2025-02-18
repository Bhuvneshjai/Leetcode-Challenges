'''
Leaf Similar Trees: Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a
leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
'''

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getLeafValues(self, root: Optional[TreeNode]) -> list[int]:
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


# Function to construct a binary tree from a list
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


# Taking input as an array
arr1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
arr2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]

root1 = constructTree(arr1)
root2 = constructTree(arr2)

sol = Solution()
print(sol.leafSimilar(root1, root2))