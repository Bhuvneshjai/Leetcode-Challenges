'''
Minimum Flips to Make a OR b Equal to c: Given 3 positives numbers a, b and c. Return the minimum flips required in some
bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

Example 1:
Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

Example 2:
Input: a = 4, b = 2, c = 7
Output: 1

Example 3:
Input: a = 1, b = 2, c = 3
Output: 0
'''


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a > 0 or b > 0 or c > 0:
            # Extract the last bits of a, b, and c
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            # Check conditions to count the flips needed
            if bit_c == 0:  # If c's bit is 0, both a and b's bits must also be 0
                flips += bit_a + bit_b
            else:  # If c's bit is 1, at least one of a or b's bits must be 1
                if bit_a == 0 and bit_b == 0:
                    flips += 1

            # Right shift a, b, and c to check the next bits
            a >>= 1
            b >>= 1
            c >>= 1

        return flips

sol = Solution()

# Example usage
result1 = sol.minFlips(2, 6, 5)  # Input example 1
result2 = sol.minFlips(4, 2, 7)  # Input example 2
result3 = sol.minFlips(1, 2, 3)  # Input example 3

# Print results
print("Result for (2, 6, 5):", result1)  # Output: 3
print("Result for (4, 2, 7):", result2)  # Output: 1
print("Result for (1, 2, 3):", result3)  # Output: 0