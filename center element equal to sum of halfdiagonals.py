"""
Given a matrix of odd order i.e(5*5). Task is to check if the center element of the matrix is equal to the individual sum of all the half diagonals.

Input:
F

Examples:

Input :
5
2 9 1 4 -2
6 7 2 11 4
4 2 9 2 4
1 9 2 4 4
0 2 4 2 5
Output :Yes
Explanation : 
Sum of Half Diagonal 1 = 2 + 7 = 9
Sum of Half Diagonal 2 = 9 + 0 = 9
Sum of Half Diagonal 3 = 11 + -2 = 9
Sum of Half Diagonal 4 = 5 + 4 = 9

Here, All the sums equal to the center element
that is mat[2][2] = 9
Input:
3
1 2 3
1 2 3
1 2 3
Output:
No
Input:
3
1 2 3
1 8 9
1 2 3
Output:
No
Input:
3
4 4 4
4 4 4
4 4 4
Output:
Yes
Input:
3
4 1 4
3 4 3
4 2 4
Output:
Yes
"""
MAX = 100
def HalfDiagonalSums( mat,  n):
    diag1_left = 0
    diag1_right = 0
    diag2_left = 0
    diag2_right = 0  
    i = 0
    j = n - 1
    while i < n: 
           
        if (i < n//2) : 
            diag1_left += mat[i][i] 
            diag2_left += mat[j][i]            
          
        elif (i > n//2) : 
            diag1_right += mat[i][i] 
            diag2_right += mat[j][i]            
        i += 1
        j -= 1
       
    return (diag1_left == diag2_right and diag2_right == diag2_left and diag1_right == diag2_left and diag2_right == mat[n//2][n//2]) 
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
      
print("Yes") if (HalfDiagonalSums(l,n)) else print("No" ) 
