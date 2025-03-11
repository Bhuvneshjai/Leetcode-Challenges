'''
Guess Number Higher or Lower: We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1
'''


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# Mocking the predefined `guess` API
def guess(num: int) -> int:
    pick = 6  # Change this to the number you want to test
    if num > pick:
        return -1  # The guessed number is too high
    elif num < pick:
        return 1  # The guessed number is too low
    else:
        return 0  # The guessed number is correct


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)

            if res == 0:  # Correct guess
                return mid
            elif res == -1:  # Too high, adjust search range
                right = mid - 1
            else:  # Too low, adjust search range
                left = mid + 1

        return -1  # Should never reach here


# Example usage:
sol = Solution()
print(sol.guessNumber(10))  # Expected output: 6
