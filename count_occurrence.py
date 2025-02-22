'''
we need to count the occurrences of each unique number and return them as a list.
'''

from collections import Counter
class Solution:
    # Using Built-in Function
    def count_occurrence_func(self, lst: list[int]) -> list[int]:
        count_dict = Counter(lst)
        print(f'Count Dict: {count_dict}')

        result = list(count_dict.values())
        return result

    # Without using Built-In Function
    def count_occurrence_no_func(self, lst: list[int]) -> list[int]:
        count_dict = {}
        for num in lst:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        return list(count_dict.values())

sol = Solution()
lst = [3,3,3,4,4,5,5,6]
result = sol.count_occurrence_func(lst)
print(f'Using Built-In Function: {result}')
result1 = sol.count_occurrence_no_func(lst)
print(f'Without using Built-In Function: {result1}')
