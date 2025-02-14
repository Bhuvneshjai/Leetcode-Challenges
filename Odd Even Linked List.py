'''
Odd Even Linked List: Given the head of a singly linked list, group all the nodes with odd indices together followed by
the nodes with even indices, and return the reordered list. The first node is considered odd, and the second node is
even, and so on. Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
'''

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if the list is empty or has only one node, return it
        if not head or not head.next:
            return head

        # Initialize pointers
        odd = head
        even = head.next
        even_head = even  # Store the head of even indexed nodes

        # Rearranging nodes
        while even and even.next:
            odd.next = even.next  # Link odd nodes together
            odd = odd.next  # Move odd pointer

            even.next = odd.next  # Link even nodes together
            even = even.next  # Move even pointer

        # Connect odd list to even list
        odd.next = even_head
        return head

# Helper function to convert a list to a linked list
def list_to_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example usage
sol = Solution()
head = list_to_linked_list([1, 2, 3, 4, 5])  # Convert list to linked list
new_head = sol.oddEvenList(head)  # Process the linked list
print(linked_list_to_list(new_head))  # Convert back to list and print result

head = list_to_linked_list([2, 1, 3, 5, 6, 4, 7])
new_head = sol.oddEvenList(head)
print(linked_list_to_list(new_head))
