"""
Given a matrix grid[][] of size Y x Y and two integers M and N, the task is to find the sum of cost of all possible paths 

from the (0, 0) to (M, N) by moving a cell down or right. Cost of each path is defined as the sum of values of the cells visited in the path.

Input:
First line indicates two integers M and N
Second line indicates the integer Y
Next Y lines indicates elements of grid
Output:
Print sum of all paths cost
Examples:

Input: 
1 1
3
1 2 3
4 5 6
7 8 9
Output:
18
Explanation:
There are only 2 ways to reach (1, 1)
Path 1: (0, 0) => (0, 1) => (1, 1)
Path cost = 1 + 2 + 5 = 8
Path 2: (0, 0) => (1, 0) => (1, 1)
Path cost = 1 + 4 + 5 = 10
Total Path Sum = 8 + 10 = 18

Input:
2 2
3
1 1 1
1 1 1
1 1 1

Output: 
30
Explanation:
Sum of path cost of all path is 30.

Input:
1 1
3
1 2 3
2 3 4
4 5 6
Output:
12

Input:
0 0
1
2
Output:
2

Input:
1 1
2
1 2
3 4
Output:
15
"""
Col = 3
def nCr(n, r):
    return fact(n) / (fact(r) * fact(n - r))

def fact(n): 
      
    res = 1
    for i in range(2, n + 1): 
        res = res * i 
    return res

def sumPathCost(grid, m, n): 
      
    sum = 0
    count = 0
    for i in range(0, m + 1): 
        for j in range(0, n + 1):
            count = (nCr(i + j, i) * nCr(m + n - i - j, m - i))
            sum += count * grid[i][j]; 
  
    return sum
  
m,n=map(int,input().split())
x=int(input())
l=[]
for i in range(x):
    l.append(list(map(int,input().split())))
print(int(sumPathCost(l, m, n)))
