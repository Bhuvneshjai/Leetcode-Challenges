'''
viod of diamond: Problem statement
You are given an integer ‘N’, ‘N’ will always be an odd integer. Your task is to print a pattern with the following
description:

1. The pattern will consist of ‘N’ lines.
2. The pattern will consist of ‘ ‘ (space) and ‘*’ characters only.
3. The pattern will be a “Void of Diamond” pattern.
4. A “Void of Diamond” pattern is a pattern ‘N’ * ‘N’ cells and ‘ ‘ characters make a diamond shape and ‘*’ fill all
other points.
5. For a better understanding of the “Void of Diamond” pattern refer to example and sample input-output.
For example:

If ‘N’ is 5 then the pattern will be-
*****
** **
*   *
** **
*****
Detailed explanation ( Input/output format, Notes, Images )

Sample Input 1:
2
5
3
Sample Output 1:
*****
** **
*   *
** **
*****
***
* *
***
Explanation of Sample Input 1:
Test Case 1:
Given ‘N’ = 5
We will print the pattern as the description of the “Void of Diamond” pattern.

Test Case 2:
Given ‘N’ = 3
There will be only 1 ‘ ‘ space in the diamond pattern.

Sample Input 2:
2
7
9
Sample Output 2:
*******
*** ***
**   **
*     *
**   **
*** ***
*******
*********
**** ****
***   ***
**     **
*       *
**     **
***   ***
**** ****
*********
Explanation of Sample Input 2:
Test Case 1:
Given ‘N' = 7
The pattern is printed such that ‘ ‘ making a diamond and ‘*’ filling other points.

Test Case 2:
Given ‘N’ = 9
Created a 9*9 grid and all space cells make a diamond pattern.
'''

def printVoidOfDiamond(n):
    for i in range(n):
        for j in range(n):
            if abs(i - n // 2) + abs(j - n // 2) < n // 2:
                print(' ', end='')
            else:
                print('*', end='')
        print()

T = int(input())
for _ in range(T):
    N = int(input())
    printVoidOfDiamond(N)
