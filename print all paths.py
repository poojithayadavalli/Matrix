"""
Given a matrix of size mXn. The problem is to print all the possible paths from top left to bottom right 

of a mXn matrix with the constraints that from each cell you can either move only to right or down.
Examples :

Input : 
1 2 3
4 5 6
Output :
1 4 5 6
1 2 5 6
1 2 3 6

Input : 
1 2 
3 4
Output : 
1 2 4
1 3 4
Input:
3 3
1 3 4
3 4 5
4 6 7
Output:
1 3 4 6 7 
1 3 4 6 7 
1 3 4 5 7 
1 3 4 6 7 
1 3 4 5 7 
1 3 4 5 7
Input:
1 2
3 4
5 6
Output:
1 3 5 6 
1 3 4 6 
1 2 4 6 
"""

def printAllPathsUtil(mat, i, j, m, n, path, pi):
    if (i == m - 1): 
        for k in range(j, n): 
            path[pi + k - j] = mat[i][k] 
  
        for l in range(pi + n - j): 
            print(path[l], end = " ") 
        print() 
        return
    if (j == n - 1): 
  
        for k in range(i, m): 
            path[pi + k - i] = mat[k][j] 
  
        for l in range(pi + m - i): 
            print(path[l], end = " ") 
        print() 
        return
    path[pi] = mat[i][j]
    printAllPathsUtil(mat, i + 1, j, m, n, path, pi + 1)
    printAllPathsUtil(mat, i, j + 1, m, n, path, pi + 1)
def printAllPaths(mat, m, n):
    path = [0 for i in range(m + n)] 
    printAllPathsUtil(mat, 0, 0, m, n, path, 0) 

mat = []
m,n=map(int,input().split())
for i in range(m):
    mat.append(list(map(int,input().split())))
printAllPaths(mat,m,n)
