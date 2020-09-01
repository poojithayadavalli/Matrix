"""
Given an N x M matrix of integers, the task is to count the number of palindromic pluses in the array.

Palindromic plus is formed when a palindromic sub-row and palindromic sub-column cross each other at the middle element.

Examples:

Input:
3 3
1 2 1
2 3 2
3 2 1
Output: 
1
Explanation:
Palindromic row from (1, 0) – > (1, 2) and Palindromic column (0, 1) -> (2, 1) form a palindromic plus.

Input:
3 4
1 2 1 3
2 3 2 3
3 2 1 4
Output: 
2
Explanation:
The palindromic pluses in the given matrix are:
"""
def countPalindromicPlus(n, m, a): 
    i, j, k = 0, 0, 0
    count = 0
    for i in range(1, n - 1): 
        for j in range(1, m - 1):
            if (a[i + 1][j] == a[i - 1][j] 
                and a[i][j - 1] == a[i][j + 1]): 
                count += 1
    return count
if __name__ == '__main__':
    n,m=map(int,input().split())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    print(countPalindromicPlus(n, m, a))
