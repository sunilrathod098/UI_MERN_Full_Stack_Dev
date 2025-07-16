# Given a set of distinct integers, print the size of a maximal subset of S where the sum of any 2 numbers in S' is not evenly divisible by k.

# Example
# S = [10, 10, 12, 10, 24, 25, 22] * k = 4
# One of the arrays that can be created is S' * [0] = [10, 12, 25] Another is S' * [1] = [19, 22, 24] After testing all permutations, the maximum length solution array has 3 elements.

# Function Description
# Complete the nonDivisibleSubset function in the editor below.
# non DivisibleSubset has the following parameter(s):
# int Sin]: an array of integers
# int k: the divisor
# Returns
# int: the length of the longest subset of S meeting the criteria

# Input Format
# The first line contains 2 space-separated integers, n and k, the number of values in S and the non factor.
# The second line contains n space-separated integers, each an S[i], the unique values of the set.

# Constraints
# 1 <= n <= 10 ^ 5
# 1 <= k <= 100
# 1 <= S[d] <= 10 ^ 0
# All of the given numbers are distinct.

# Sample InputSTDIN
# Function
# 43
# S[] size n = 4, k = 3
# 1724 S= [1, 7, 2, 4]

# Sample Output
# 3

# Explanation
# scussions
# The sums of all permutations of two elements from S = (1, 7, 2, 4} are:
# 1+7=8
# 1+2=3
# 1+4=5
# 7+2=9
# 7+4=11
# 2+4=6

# Editorial
# F1
# Only S = {1,7, 4} will not ever sum to a multiple of k = 3.



# Code

# import math
# import os
# import random
# import re
# import sys

# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s


def nonDivisibleSubset(k, s):
    # Write your code here
    remainder_counts = [0] * k
    for num in s:
        remainder_counts[num % k] += 1
        
    count = min(remainder_counts[0],1)
    
    for r in range(1, (k//2) + 1):
        if r == k- r:
            count += min(remainder_counts[r], 1)
        else:
            count += max(remainder_counts[r], remainder_counts[k-r])
            
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')
    fptr.close()
