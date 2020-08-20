"""
Given a MxM matrix consisting of positive integers, the task is to find the minimum number of steps 

required to reach the end(leftmost-bottom cell) of the matrix. If we are at cell (i, j) we can go to cells 

(i, j+arr[i][j]) or (i+arr[i][j], j). We can not go out of bounds. If no path exists, print -1.

Examples:

Input : 
3
2 1 2
1 1 1
1 1 1
Output : 2
Explanation : 
The path will be {0, 0} -> {0, 2} -> {2, 2}
Thus, we are reaching end in two steps.

Input :
3
1 1 2
1 1 1
2 1 1
Output : 
3
Input:
3
1 2 3
1 2 3
1 2 3
Output:
-1
Input:
3
1 2 1
1 1 1
2 2 1
Output:
3
Input:
2
1 1
2 1
Output:
2
"""
import numpy as np
n = int(input()) 
dp = np.zeros((n, n))  
v = np.zeros((n, n)) 
def minSteps(i, j, arr) :
    if (i == n - 1 and j == n - 1) : 
        return 0
    if (i > n - 1 or j > n - 1) : 
        return 9999999 
    if (v[i][j]) : 
        return dp[i][j]
  
    v[i][j] = 1 
    dp[i][j] = 1 + min(minSteps(i + arr[i][j], j, arr),minSteps(i, j + arr[i][j], arr));
    return dp[i][j] 
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))            
ans = minSteps(0, 0, arr) 
if (ans >= 9999999) : 
    print(-1)   
else : 
    print(ans)
