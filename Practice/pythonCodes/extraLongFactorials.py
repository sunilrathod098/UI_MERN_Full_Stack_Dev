# The factorial of the integer n. written n!, is defined as:
# n! = n x (n-1) × (n-2)x×3×2×1
# Calculate and print the factorial of a given integer.
# For example, if n = 30. we calculate 30 x 29 x 28 x x 2 x 1 and get 265252859812191058636308480000000.

# Function Description
# Complete the extraLongFactorials function in the editor below. It should print the result and return.
# extraLongFactorials has the following parameter(s):
# n: an integer
# Note: Factorials of n > 20 can't be stored even in a 64-bit long long variable. Big integers must used for such calculations. Languages like Java, Python, Ruby etc. can handle big integers, but we need to write additional code in C/C++ to handle huge values.
# We recommend solving this challenge using BigIntegers.

# Input Format
# Input consists of a single integer n

# Constraints
# 1 ≤ n ≤100

# Output Format
# Print the factorial of n.

# Sample Input
# 25

# Sample Output
# 1551121004333098598-4000000

# Explanation
# 25!25 x 24x23x3x2x1

# Code

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    if n == 1:
        return 1
    else:
        factorial =  n * extraLongFactorials(n - 1)

        return factorial

        
if __name__ == '__main__':
    n = int(input().strip())

    print(extraLongFactorials(n))



# Output

# Input:-
# 25
# Your Output
# 15511210043330985984000000
# Expected Output
# 15511210043330985984000000


# Input:-
# 45
# Your Output (stdout)
# 119622220865480194561963161495657715064383733760000000000
# Expected Output
# 119622220865480194561963161495657715064383733760000000000