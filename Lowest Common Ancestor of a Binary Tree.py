'''
Lowest Common Ancestor of a Binary Tree: Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree. According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes
p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1
'''


# Definition for a binary tree node.
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

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right


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

# Create an instance of Solution
sol = Solution()

# Example usage
values1 = [3,5,1,6,2,9,8,None,None,7,4]
values2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]

# Construct trees from lists
root1 = constructTree(values1)
root2 = constructTree(values2)

# Check if the trees are leaf-similar
print(sol.leafSimilar(root1, root2))  # Output: True or False

