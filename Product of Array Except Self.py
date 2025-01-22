''' Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32 - bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example:
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Example:
Input: nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.) '''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1]*n
        print(result)
        print()

        prefix=1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        print(result)
        print(prefix)

        suffix=1
        for i in range(n-1,-1,-1):
            result[i] *= suffix
            suffix *= nums[i]
        print(result)
        print(suffix)

        return result

nums = [1, 2, 3, 4]
solution = Solution()
print(solution.productExceptSelf(nums))
