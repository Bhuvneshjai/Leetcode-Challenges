# Reverse Words in a String
""" Given an input string s, reverse the order of the words. A word is defined as a sequence of non - space characters.
The words in s will be separated by at least one space. Return a string of the words in reverse order concatenated by
a single space. Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned
string should only have a single space separating the words. Do not include any extra spaces.

Example:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example:
Input: s = "  hello world  "
Output: "world hello"

Explanation: Your reversed string should not contain leading or trailing spaces.

Example:
Input: s = "a good   example"
Output: "example good a"

Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Constraints:
1 <= s.length <= 104

Follow - up: If the string data type is mutable in your language, can you solve it in -place with O(1) extra space? """

# Code-1:
class Solution1:
    def reverseWords(self, s:str) -> str:
        # Leading and Trailing whitespaces from the string and split into the list of words based on the space.
        s1 = s.strip().split()
        # Reverse the list of words.
        s1 = s1[::-1]
        # Joins the reversed list of words into a single string with a space as a separator.
        return " ".join(s1)

sol1 = Solution1()
res1 = sol1.reverseWords("    Hello World  ")
print(f"Result-1: {res1}")

# ------------------------------------------------------------------------------------------------------------------------
# Code-2:
class Solution2:
    def reverseWords(self, s:str) -> str:
        return " ".join(reversed(s.strip().split()))

sol2 = Solution2()
res2 = sol2.reverseWords("Hello World")
print(f"Result-2: {res2}")

# ------------------------------------------------------------------------------------------------------------------------
# Code-3:
class Solution3:
    def reverseWords(self, s:str) -> str:
        words = s.strip().split()
        n = len(words)
        for i in range(n//2):
            words[i], words[n-i-1] = words[n-i-1], words[i]
        return " ".join(words)

sol3 = Solution3()
res3 = sol3.reverseWords("Hello             World")
print(f"Result-3: {res3}")

