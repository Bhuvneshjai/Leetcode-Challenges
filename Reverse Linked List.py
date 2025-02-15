'''
Reverse Linked List: Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
'''

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

# Helper function to convert a list to a linked list
def list_to_linked_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example usage
sol = Solution()
head = list_to_linked_list([1, 2, 3, 4, 5])  # Convert list to linked list
new_head = sol.reverseList(head)  # Process the linked list using reverseList
print(linked_list_to_list(new_head))  # Convert back to list and print result

head = list_to_linked_list([2, 1, 3, 5, 6, 4, 7])
new_head = sol.reverseList(head)
print(linked_list_to_list(new_head))
