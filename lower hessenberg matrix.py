"""
Given a matrix of order NxN, Find the minimum number of steps to convert given matrix into Lower Hessenberg matrix. 

In each step, the only operation allowed is to decrease or increase any element value by 1.

Examples:

Input:
3
1 2 8
1 3 4
2 3 4
Output: 
8
Decrease the element a[0][2] 8 times.
Now the matrix is lower Hessenberg.

Input:
4
9 2 5 5
12 3 4 5
13 -3 4 2
-1 10 1 4
Output:
15
Input:
3
1 2 3
1 2 3
4 5 6
Output:
3
Input:
3
3 4 5
-1 -1 -3
-3 4 5
Output:
5
Input:
3
1 2 3
7 8 9
7 6 10
Output:
3
"""
N = int(input())
def stepsRequired(arr): 
    result = 0
    for i in range(N): 
        for j in range(N): 
            if (j > i + 1): 
                result += abs(arr[i][j]) 
    return result
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
print(stepsRequired(arr))
