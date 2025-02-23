'''
Binary Tree Right Side View: Given the root of a binary tree, imagine yourself standing on the right side of it, return
the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]

Example 3:
Input: root = [1,null,3]
Output: [1,3]

Example 4:
Input: root = []
Output: []
'''


# Definition for a binary tree node.
from typing import Optional, List
from collections import deque

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

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


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

sol = Solution()

# Test Case 1
root1 = constructTree([1, 2, 3, None, 5, None, 4])
print(sol.rightSideView(root1))  # Expected output: [1, 3, 4]

# Test Case 2
root2 = constructTree([1, 2, 3, 4, None, None, None, 5])
print(sol.rightSideView(root2))  # Expected output: [1, 3, 4, 5]

# Test Case 3
root3 = constructTree([1, None, 3])
print(sol.rightSideView(root3))  # Expected output: [1, 3]

# Test Case 4: Single node tree
root4 = constructTree([1])
print(sol.rightSideView(root4))  # Expected output: [1]

# Test Case 5: Empty tree
root5 = constructTree([])
print(sol.rightSideView(root5))  # Expected output: []

# Test Case 6: All nodes have only left children
root6 = constructTree([1, 2, None, 3, None, 4, None])
print(sol.rightSideView(root6))  # Expected output: [1, 2, 3, 4]

# Test Case 7: All nodes have only right children
root7 = constructTree([1, None, 2, None, 3, None, 4])
print(sol.rightSideView(root7))  # Expected output: [1, 2, 3, 4]
