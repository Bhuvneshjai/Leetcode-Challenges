# Approach-1: Simple
def compareTriplets(a,b):
    score_a = 0
    score_b = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            score_a += 1
        elif a[i] < b[i]:
            score_b += 1

    return [score_a, score_b]

# Summary
# Time Complexity: O(n)
# Space Complexity: O(1)

# Approach-2: Recursion
def compareTriplets1(a,b,index=0,score_a=0,score_b=0):
    if index == len(a):
        return [score_a,score_b]

    if a[index] > b[index]:
        score_a += 1
    elif a[index] < b[index]:
        score_b += 1

    return compareTriplets1(a,b,index+1,score_a,score_b)

# Summary
# Time Complexity: O(n)
# Space Complexity: O(n)

if __name__ == '__main__':
    a = list(map(int, input("Enter Number A: ").rstrip().split()))
    b = list(map(int, input("Enter Number B: ").rstrip().split()))

    result= compareTriplets(a,b)
    print(f"Result (simple): {result}")

    result1 = compareTriplets1(a,b)
    print(f"Result (recursive) : {result1}")