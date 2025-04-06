'''
Planet Division: Problem statement
Odin has 'N' planet in his realm, and he wanted to distribute it between his two children, Thor and Loki. He can give any
planet to only one of his children, either Loki or Thor.

He loves Thor more than Loki, so he wants Thor will get more planets than Loki, but at the same time, he also wanted that
the absolute difference in the number of planets between his children is the minimum possible.

Find the number of planets Thor and Loki get, respectively.

Example:
'N' = 7
The minimum possible absolute difference between the number of planets is 1 when 7 is divided into 4 and 3  or 7 is
divided into 3 and 4. Odin has to give more planets to Thor.
So, Odin will give 4 planets to Thor and 3 to Loki.
Hence, the answer for this case is 4 3.
Detailed explanation ( Input/output format, Notes, Images )

Constraints:
1 ≤ T ≤ 10^5
1 ≤ N ≤ 10^9
Time limit: 1 sec

Sample Input 1:
2
8
6
Sample Output 1 :
4 4
3 3
Explanation For Sample Input 1 :

For test case 1:
When Odin divides planets between his children, the minimum possible absolute difference is 0.
Thus, Odin will give 4 planets to Thor and Loki each.

For test case 2:
When Odin divides planets between his children, the minimum possible absolute difference is 0.
Thus, Thor and Loki will receive 3 planets from Odin each.

Sample Input 2 :
2
9
7
Sample Output 2 :
5 4
4 3
'''

from typing import *


def planetDivision(n: int) -> List[int]:
    thor = (n+1)//2
    loki = n//2
    return [thor, loki]

T = int(input())
for _ in range(T):
    n = int(input())
    result = planetDivision(n)
    print(result[0], result[1])