'''
Decode String: Problem statement
An encoded string 'S' of lowercase letters with some hidden message is given to you in an interview. The string is encoded
in the following way:

The ASCII value of the characters of the original string is decreased by one, and the character with the new ASCII value
is written at that position. And the character 'a' is replaced by the character 'z'.
FInd the original string and return it.

Example:
'S' = 'abc'
Encoded string is 'abc', and the ASCII value of 'a', 'b', and 'c' is, respectively, '97', '98', and '99'.
After increasing the each ASCII value by one, the new ASCII values are '98', '99', and '100' which correspond to the
characters 'b', 'c', and 'd'.

So, the original string is 'bcd'.
Detailed explanation ( Input/output format, Notes, Images )

Constraints :
1 <= T <= 10
1 <= |S| <= 10^5, |S| denotes length of the string 'S'
Time Limit: 1 sec

Sample Input 1:
2
bnchmf
mhmizr

Sample Output 1:
coding
ninjas
Explanation Of Sample Input 1:

For test case 1:
Encoded string 'S' is 'bnchmf'. ASCII values of each character are:
'b' → 98, after increasing by one 99 → 'c'
'n' → 110, after increasing by one 111 → 'o'
'c' → 100, after increasing by one 101 → 'd'
'h' → 104, after increasing by one 105 → 'i'
'm' → 109, after increasing by one 110 → 'n'
'f' → 102, after increasing by one 103 → 'g'
So, the answer is 'coding'.

For test case 2:
Encoded string 'S' is 'mhmizr'. ASCII values of each character are:
'm' → 109, after increasing by one 110 → 'n'
'h' → 104, after increasing by one 104 → 'i'
'm' → 109, after increasing by one 110 → 'n'
'i' → 105, after increasing by one 106 → 'j'
'z' → 122, decoded as 'a'.
'r' → 114, after increasing by one 115 → 's'
So, the answer is 'ninjas'.

Sample Input 2:
2
gdkkn
vnqkc

Sample Output 2:
hello
world
'''

from typing import List
def decodeString(s: str) -> str:
    decoded = []
    for char in s:
        if char == 'z':
            decoded.append('a')
        else:
            decoded.append(chr(ord(char)+1))
    return ''.join(decoded)

T = int(input())
for _ in range(T):
    encoded = input().strip()
    print(decodeString(encoded))
