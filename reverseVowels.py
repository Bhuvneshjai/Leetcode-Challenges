class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAeiou")                  # Define Vowels in Both Lower Case and Upper Case
        s_lst = list(s)                             # Convert the string to a list
        print(f"List of {s} : {s_lst}")        # Print list
        i,j = 0, len(s)-1                           # Initialize 2 pointers

        while i < j:
            if s_lst[i] in vowels and s_lst[j] in vowels:
                s_lst[i], s_lst[j] = s_lst[j], s_lst[i]     # Swaps the vowels
                i += 1
                j -= 1
            elif s_lst[i] not in vowels:
                i += 1                              # Move the left pointer forward
            elif s_lst[j] not in vowels:
                j -= 1                              # Move the right pointer backward
        return "".join(s_lst)

solution = Solution()
result = solution.reverseVowels("hello")
print(f"Reverse Vowels String : {result}")
