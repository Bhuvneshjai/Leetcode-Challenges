'''
Kth Largest Element in an Array: Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

from heapq import heapify, heappush, heappop
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []  # Min heap to store top k largest elements

        for num in nums:
            heappush(min_heap, num)  # Insert element into heap
            if len(min_heap) > k:  # Keep heap size at k
                heappop(min_heap)  # Remove smallest element

        return min_heap[0]  # Root of heap is the kth largest element

sol = Solution()

# Example 1
print(sol.findKthLargest([3,2,1,5,6,4], 2))  # Output: 5

# Example 2
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))  # Output: 4

# Edge Case 1: Single element
print(sol.findKthLargest([1], 1))  # Output: 1

# Edge Case 2: Already sorted descending
print(sol.findKthLargest([10, 9, 8, 7, 6, 5, 4], 3))  # Output: 8
