'''
Delete Node in a BST: Given a root node reference of a BST and a key, delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
Search for a node to remove. If the node is found, delete the node.

Example 1:
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:
Input: root = [], key = 0
Output: []
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found, handle deletion
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Node has two children: find the inorder successor (smallest in the right subtree)
            successor = self.findMin(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node


from collections import deque
from typing import List, Optional

# Helper function to construct a BST from a list
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

# Helper function to convert a BST to a list (level-order traversal)
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

# Test Case 1: Deleting node 3 from BST [5,3,6,2,4,None,7]
root1 = constructBST([5, 3, 6, 2, 4, None, 7])
result1 = sol.deleteNode(root1, 3)
print(treeToList(result1))  # Expected Output: [5,4,6,2,None,None,7] OR [5,2,6,None,4,None,7]

# Test Case 2: Deleting node 0 which is not present in BST [5,3,6,2,4,None,7]
root2 = constructBST([5, 3, 6, 2, 4, None, 7])
result2 = sol.deleteNode(root2, 0)
print(treeToList(result2))  # Expected Output: [5,3,6,2,4,None,7] (unchanged)

# Test Case 3: Deleting from an empty tree
root3 = constructBST([])
result3 = sol.deleteNode(root3, 0)
print(treeToList(result3))  # Expected Output: []

# Test Case 4: Deleting the root node in a single-node tree
root4 = constructBST([5])
result4 = sol.deleteNode(root4, 5)
print(treeToList(result4))  # Expected Output: []

# Test Case 5: Deleting a node with only one child
root5 = constructBST([5,3,6,2,None,None,7])
result5 = sol.deleteNode(root5, 3)
print(treeToList(result5))  # Expected Output: [5,2,6,None,None,None,7]

# Test Case 6: Deleting the root node in a tree with two children
root6 = constructBST([5,3,6,2,4,None,7])
result6 = sol.deleteNode(root6, 5)
print(treeToList(result6))  # Expected Output: [6,3,7,2,4]

