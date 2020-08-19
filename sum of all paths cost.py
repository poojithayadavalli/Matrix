"""
Given a matrix grid[][] and two integers M and N, the task is to find the sum of cost of all possible paths from the (0, 0) to (M, N) by moving a cell down or right. Cost of each path is defined as the sum of values of the cells visited in the path.

Examples:

Input: M = 1, N = 1, grid[][] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
Output: 18
Explanation:
There are only 2 ways to reach (1, 1)
Path 1: (0, 0) => (0, 1) => (1, 1)
Path cost = 1 + 2 + 5 = 8
Path 2: (0, 0) => (1, 0) => (1, 1)
Path cost = 1 + 4 + 5 = 10
Total Path Sum = 8 + 10 = 18

Input: M = 2, N = 2, grid = { {1, 1, 1}, {1, 1, 1}, {1, 1, 1} }
Output: 30
Explanation:
Sum of path cost of all path is 30.
"""
