'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Create a DP table with dimensions (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize the DP table
        for i in range(m + 1):
            dp[i][0] = i  # Cost of deleting all characters from word1
        for j in range(n + 1):
            dp[0][j] = j  # Cost of inserting all characters into word1

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # Characters match; no operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Minimum of insert, delete, or replace operation
                    dp[i][j] = 1 + min(dp[i - 1][j],    # Delete
                                       dp[i][j - 1],    # Insert
                                       dp[i - 1][j - 1])  # Replace

        # Return the minimum number of operations
        return dp[m][n]

word1 = "horse"
word2 = "ros"

solution = Solution()
print(solution.minDistance(word1, word2))  # Output: 3

