'''
Best Time to Buy and Sell Stock with Transaction Fee: You are given an array prices where prices[i] is the price of a
given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the
transaction fee for each transaction.

Note:
You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.

Example 1:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
'''


class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        # Initialize variables to track cash (profit) and stock holdings
        cash = 0  # Maximum profit if no stock is held
        hold = -prices[0]  # Maximum profit if stock is held (negative because we buy)

        # Iterate through each day's price
        for price in prices:
            # Update cash: profit if we sell the stock today
            cash = max(cash, hold + price - fee)
            # Update hold: profit if we buy the stock today or continue holding
            hold = max(hold, cash - price)

        # Return the maximum profit when no stock is held
        return cash

prices = [1, 3, 7, 5, 10, 3]
fee = 3

solution = Solution()
print(solution.maxProfit(prices, fee))  # Output: 6
