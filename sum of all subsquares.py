"""
Given an n x n square matrix and integer k .Task is as follows:

find sum of all sub-squares of size k x k where k is smaller than or equal to n.
Examples :

Input:
5
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
3
Output:
18  18  18
27  27  27
36  36  36


Input:
3
1 2 3
4 5 6
7 8 9
2
Output:
12  16
24  28
Input:
3
1 2 3
1 2 3
1 2 3
2
Output:
6 10 
6 10 

"""
def printSumTricky(mat, k): 
    global n
    if k > n: 
        return
    stripSum = [[None] * n for i in range(n)]
    
    for j in range(n): 
        Sum = 0
        for i in range(k): 
            Sum += mat[i][j]  
        stripSum[0][j] = Sum
        
        for i in range(1, n - k + 1): 
            Sum += (mat[i + k - 1][j] -
                    mat[i - 1][j])  
            stripSum[i][j] = Sum
            
    for i in range(n - k + 1):
        Sum = 0
        for j in range(k): 
            Sum += stripSum[i][j]  
        print(Sum, end = " ")
        for j in range(1, n - k + 1): 
            Sum += (stripSum[i][j + k - 1] -
                    stripSum[i][j - 1])  
            print(Sum, end = " ") 
  
        print() 
  
# Driver Code 
n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))
k = int(input())
printSumTricky(mat, k)
