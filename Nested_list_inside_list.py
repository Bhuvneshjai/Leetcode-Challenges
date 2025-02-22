'''
To flatten a nested list of unknown depth, we need a recursive approach because we don't know how deep the nesting goes.
'''
# Using Recursive Approach
'''
🔹 How It Works? (Step-by-Step)
1. Start with the input list:
[1, 2, [3, 4, 5, [6, 7, [8]]], 9]

2. The function iterates through each item:
If the item is a list, call flatten_list() recursively.
If the item is not a list, add it to flat_list.

3. The recursion breaks down lists until all elements are added to flat_list.

🔹 Recursive Breakdown
First Call:
flatten_list([1, 2, [3, 4, 5, [6, 7, [8]]], 9])
1 → Not a list → Append → [1]
2 → Not a list → Append → [1, 2]
[3, 4, 5, [6, 7, [8]]] → List → Recursive Call

Second Call:
flatten_list([3, 4, 5, [6, 7, [8]]])
3 → Append → [1, 2, 3]
4 → Append → [1, 2, 3, 4]
5 → Append → [1, 2, 3, 4, 5]
[6, 7, [8]] → List → Recursive Call

Third Call:
flatten_list([6, 7, [8]])
6 → Append → [1, 2, 3, 4, 5, 6]
7 → Append → [1, 2, 3, 4, 5, 6, 7]
[8] → List → Recursive Call

Fourth Call:
flatten_list([8])
8 → Append → [1, 2, 3, 4, 5, 6, 7, 8]
Recursion ends and returns the final flattened list.
'''
class Solution:
    def flatten_list(self, nested_list) -> list:
        flat_list = []
        for item in nested_list:
            if isinstance(item, list):
                flat_list.extend(self.flatten_list(item))
            else:
                flat_list.append(item)
        return flat_list

sol = Solution()
lst = [1, 2, [3, 4, 5, [6, 7, [8]]], 9]
result = sol.flatten_list(lst)
print(f"Using Recursive Approach: {result}")


# without using function
'''
🔹 How It Works? (Step-by-Step)
Instead of recursion, we use a stack (LIFO: Last In, First Out).
We reverse the input list before processing to maintain order.
We pop elements from the stack:
    If the popped item is a list, extend it in reversed order.
    If the popped item is a single value, append it to flat_list.
    
🔹 Stack Execution
Initial State:
stack = [9, [3, 4, 5, [6, 7, [8]]], 2, 1]  # (Reversed Input)

Iteration 1:
stack.pop() → 1
flat_list = [1]

Iteration 2:
stack.pop() → 2
flat_list = [1, 2]

Iteration 3:
stack.pop() → [3, 4, 5, [6, 7, [8]]]

This is a list, so extend the stack with reversed elements
stack = [9, [6, 7, [8]], 5, 4, 3]

Iteration 4:
stack.pop() → 3
flat_list = [1, 2, 3]

Iteration 5:
stack.pop() → 4
flat_list = [1, 2, 3, 4]

Iteration 6:
stack.pop() → 5
flat_list = [1, 2, 3, 4, 5]

Iteration 7:
stack.pop() → [6, 7, [8]]

Extend stack:
stack = [9, [8], 7, 6]

Iteration 8:
stack.pop() → 6
flat_list = [1, 2, 3, 4, 5, 6]

Iteration 9:
stack.pop() → 7
flat_list = [1, 2, 3, 4, 5, 6, 7]

Iteration 10:
stack.pop() → [8]

Extend stack
stack = [9, 8]

Iteration 11:
stack.pop() → 8
flat_list = [1, 2, 3, 4, 5, 6, 7, 8]

Iteration 12:
stack.pop() → 9
flat_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

flat_list = []
stack = lst[::-1]
print(f'stack: {stack}')
while stack:
    item = stack.pop()
    if isinstance(item, list):
        stack.extend(item[::-1])
    else:
        flat_list.append(item)
print(f'Using Without Function: {flat_list}')