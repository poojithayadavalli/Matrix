"""
Given an N x M matrix of integers, the task is to count the number of palindromic pluses in the array.

Palindromic plus is formed when a palindromic sub-row and palindromic sub-column cross each other at the middle element.

Examples:

Input: matrix = [[1, 2, 1], [2, 3, 2], [3, 2, 1]]
Output: 1
Explanation:
Palindromic row from (1, 0) – > (1, 2) and Palindromic column (0, 1) -> (2, 1) form a palindromic plus.

Input: matrix = [[1, 2, 1, 3], [2, 3, 2, 3], [3, 2, 1, 4]
Output: 2
Explanation:
The palindromic pluses in the given matrix are:
"""
