from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]

# Create an object of Solution
solution = Solution()

# Example input
candies = [2, 3, 5, 1, 3]
extraCandies = 3

# Call the function
result = solution.kidsWithCandies(candies, extraCandies)

# Print the result
print(result)
