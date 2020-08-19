"""
Given a binary matrix mat[][] of size NxM and two integers X and Y, the task is to find the minimum number steps required to move all 1’s in the given matrix to the cell (X, Y), where, one step involves moving a cell left, right, up or down.
Examples: 

Input: mat[][] = { {1, 0, 1}, {0, 1, 0}, {1, 0, 1} }, X = 1, Y = 1 
Output: 8 
Explanation: 
Cells (0, 0), (0, 2), (1, 1), (2, 0) and (2, 2) consists of 1. 
Moving 1 at index (0, 0) to (1, 1) requires 2 steps 
(0, 0) -> (0, 1) ->(1, 0) 
Moving 1 at index (0, 2) to (1, 1) requires 2 steps 
Moving 1 at index (2, 0) to (1, 1) requires 2 steps 
Moving 1 at index (2, 2) to (1, 1) requires 2 steps 
Therefore, 8 steps are required.

Input: mat[][] = { {1, 0, 0, 0}, {0, 1, 0, 1}, {1, 0, 1, 1} }, X = 0, Y = 2 
Output: 15 
"""
