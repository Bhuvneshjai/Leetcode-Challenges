'''
House Robber: You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge cases: if there are no houses or just one house
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Initialize two variables to keep track of the max profit
        prev2 = 0  # Maximum money robbed from houses till two steps before
        prev1 = 0  # Maximum money robbed till the previous house

        # Iterate through each house's money
        for num in nums:
            # Calculate the maximum money for the current house
            current = max(prev1, prev2 + num)
            # Update prev2 and prev1 for the next iteration
            prev2 = prev1
            prev1 = current

        # The result is stored in prev1
        return prev1

nums = [1, 2, 3, 1]
sol = Solution()
print(sol.rob(nums))  # Output: 4

