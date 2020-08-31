"""
Given a 2D square matrix, the task is to print the Principal and Secondary diagonals of this matrix in O(N) time complexity.

Examples :

Input: 
4
1 2 3 4
4 3 2 1
7 8 9 6
6 5 4 3
Output:
1 3 9 3
4 2 8 6
Explanation:
Principal Diagonal: 1, 3, 9, 3
Secondary Diagonal: 4, 2, 8, 6

Input:
3
1 1 1
1 1 1
1 1 1
Output:
1 1 1
1 1 1
Input:
3
1 2 3
1 2 3
1 2 3
Output:
1 2 3 
3 2 1
"""

MAX = 100; 
  
# Function to print the Principal Diagonal 
def printPrincipalDiagonal(mat, n):
    for i in range(n):
        print(mat[i][i],end= " ")
    print()
  
# Function to print the Secondary Diagonal 
def printSecondaryDiagonal(mat, n):
    for i in range(n): 
        print(mat[i][n - i - 1], end = " ")
if __name__ == '__main__': 
    n = int(input())
    a =[ ]
    for i in range(n):
        a.append(list(map(int,input().split())))
    printPrincipalDiagonal(a, n) 
    printSecondaryDiagonal(a, n)
