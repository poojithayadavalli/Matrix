"""
Given a binary matrix mat[][] of size NxM and two integers X and Y, the task is to find the minimum number steps required

to move all 1’s in the given matrix to the cell (X, Y), where, one step involves moving a cell left, right, up or down.

Input:
First line contains integer N and integer M
Next N lines contains elements of matrix
Next line contains integer X and integer Y
Output:
Print the minimum number of steps required
Examples: 

Input:
3 3
1 0 1
0 1 0
1 0 1
1 1
Output:
8 
Explanation: 
Cells (0, 0), (0, 2), (1, 1), (2, 0) and (2, 2) consists of 1. 
Moving 1 at index (0, 0) to (1, 1) requires 2 steps 
(0, 0) -> (0, 1) ->(1, 0) 
Moving 1 at index (0, 2) to (1, 1) requires 2 steps 
Moving 1 at index (2, 0) to (1, 1) requires 2 steps 
Moving 1 at index (2, 2) to (1, 1) requires 2 steps 
Therefore, 8 steps are required.

Input:
3 4
1 0 0 0
0 1 0 1
1 0 1 1
0 2 
Output: 
15 
Input:
3 3
1 2 1
3 2 1
3 2 4
2 2
Output:
7
Input:
2 3
1 2 1
2 1 1
1 1
Output:
5
Input:
2 3
1 1 1
2 2 2
0 1
Output:
2
"""
def findAns(mat, x, y, n, m):
    ans = 0
    for i in range(n):  
        for j in range(m): 
            if (mat[i][j] == 1):  
                ans += (abs(x - i) + abs(y - j))
    return ans  
m,n=map(int,input().split())
mat = []
for i in range(m):
    mat.append(list(map(int,input().split())))
x,y=map(int,input().split()) 
print(findAns(mat, x, y, m, n))

