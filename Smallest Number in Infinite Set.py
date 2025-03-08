'''
Smallest Number in Infinite Set: You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.


Example 1:
Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
'''


import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.current = 1  # The smallest number available
        self.added_back = set()  # Set to track numbers added back
        self.min_heap = []  # Min-heap to keep track of added back numbers

    def popSmallest(self) -> int:
        if self.min_heap:  # If there are numbers in the heap, pop the smallest
            smallest = heapq.heappop(self.min_heap)
            self.added_back.remove(smallest)
            return smallest
        else:
            self.current += 1
            return self.current - 1  # Return the smallest number and increment current

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added_back:
            heapq.heappush(self.min_heap, num)
            self.added_back.add(num)

# Example usage:
sol = SmallestInfiniteSet()
sol.addBack(2)
print(sol.popSmallest())  # 1
print(sol.popSmallest())  # 2
print(sol.popSmallest())  # 3
sol.addBack(1)
print(sol.popSmallest())  # 1
print(sol.popSmallest())  # 4
print(sol.popSmallest())  # 5
