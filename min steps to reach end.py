"""
Given a 2d-matrix consisting of positive integers, the task is to find the minimum number of steps required to reach the end(leftmost-bottom cell) of the matrix. If we are at cell (i, j) we can go to cells (i, j+arr[i][j]) or (i+arr[i][j], j). We can not go out of bounds. If no path exists, print -1.

Examples:

Input : 
mat[][] = {{2, 1, 2},
           {1, 1, 1},
           {1, 1, 1}}
Output : 2
Explanation : The path will be {0, 0} -> {0, 2} -> {2, 2}
Thus, we are reaching end in two steps.

Input :
mat[][] = {{1, 1, 2},
           {1, 1, 1},
           {2, 1, 1}}
Output : 3
"""
