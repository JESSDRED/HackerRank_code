'''
    Hacker rank medium Array Manipulation
    Difference array to reduce time complexity
'''
# Original
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
# It may run out of time because the overall time complexity is O(n*q)
# where n is the size of the list and q is the number of queries.
def arrayManipulation(n, queries):
    # Write your code here
    List = [0] * n
    for query in queries:
        a = query[0]
        b = query[1]
        k = query[2]
        List[a-1: b-1] = [x + k for x in List[a-1:b-1]] 
    return max(List)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()


'''
    To improve the time complexity, you can use a difference array technique, which is commonly used for efficient range updates.
    Instead of updating every element in the range [a, b], we maintain a delta array (difference array) where we:
    Add k at the start index a-1 (because we're working with 0-based indexing).
    Subtract k at index b (because b is the index just after the range).
    After processing all queries, you can compute the final values of the array by accumulating the changes from the difference array.
    Thus, the overall time complexity is O(n + q), 
    where n is the size of the list and q is the number of queries. This is much more efficient than repeatedly updating the entire sublist for each query.
'''

def arrayManipulation(n, queries):
    # Write your code here
    List = [0] * (n+1)
    for query in queries:
        a = query[0]
        b = query[1]
        k = query[2]
        List[a-1] += k
        if b < (n+1):
            List[b] -= k 
    Max = 0
    Current = 0
    for i in range(n):
        Current += List[i]
        Max = max(Max,Current)       
    return Max    