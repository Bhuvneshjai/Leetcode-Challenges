'''
Search Suggestions System: You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. S
uggested products should have common prefix with searchWord. If there are more than three products with a common prefix
return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],
["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the search word.
'''

from typing import List
import bisect


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Sort products lexicographically
        products.sort()
        result = []
        prefix = ""

        for char in searchWord:
            prefix += char
            # Find the leftmost index where `prefix` could be inserted in sorted list
            index = bisect.bisect_left(products, prefix)
            # Collect up to 3 words that match the prefix
            suggestions = []
            for i in range(index, min(index + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break  # Stop when we find a word that doesn't match
            result.append(suggestions)

        return result


# Example Usage:
solution = Solution()
print(solution.suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))
