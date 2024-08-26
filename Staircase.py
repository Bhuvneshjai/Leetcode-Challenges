# https://www.hackerrank.com/contests/mountblue-technologies/challenges/staircase

import math
import os
import random
import re
import sys

# Complete the 'staircase' function below.
# The function accepts INTEGER n as parameter.

# Approach - 1
def staircase1(n):
    # Write your code here
    for i in range(1,n+1):
        print(" " * (n-i) + "#" * i)

# Summary
# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Approach - 2
def staircase2(n):
    for i in range(1,n+1):
        print(f"{' ' * (n-i)}{'#' * i}")

# Summary
# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Approach - 3


if __name__ == '__main__':
    n1 = int(input("Enter number for Approach - 1: ").strip())
    staircase1(n1)
    n2 = int(input("Enter number for Approach - 2: ").strip())
    staircase2(n2)

