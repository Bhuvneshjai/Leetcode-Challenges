'''
Search in a Binary Search Tree: You are given the root of a binary search tree (BST) and an integer val. Find the node
in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist,
return null.

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []
'''


# Definition for a binary tree node.
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


# Helper function to construct a binary search tree from a list
from collections import deque
from typing import List, Optional


def constructBST(values: List[Optional[int]]) -> Optional[TreeNode]:
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


# Helper function to convert a tree into a list (level-order)
def treeToList(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []

    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result

sol = Solution()

# Test Case 1: Searching for 2 in BST [4,2,7,1,3]
root1 = constructBST([4, 2, 7, 1, 3])
result1 = sol.searchBST(root1, 2)
print(treeToList(result1))  # Expected Output: [2, 1, 3]

# Test Case 2: Searching for 5 in BST [4,2,7,1,3]
root2 = constructBST([4, 2, 7, 1, 3])
result2 = sol.searchBST(root2, 5)
print(treeToList(result2))  # Expected Output: []

# Test Case 3: Searching for the root node (4)
root3 = constructBST([4, 2, 7, 1, 3])
result3 = sol.searchBST(root3, 4)
print(treeToList(result3))  # Expected Output: [4, 2, 7, 1, 3]

# Test Case 4: Searching in an empty tree
root4 = constructBST([])
result4 = sol.searchBST(root4, 1)
print(treeToList(result4))  # Expected Output: []

# Test Case 5: Searching for a leaf node (3)
root5 = constructBST([4, 2, 7, 1, 3])
result5 = sol.searchBST(root5, 3)
print(treeToList(result5))  # Expected Output: [3]
