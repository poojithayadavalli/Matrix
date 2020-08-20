"""
Given an array arr[] of N positive integers, the task is to find the minimum steps to reduce all the elements to 0.

In a single step, -1 can be added to all the non-zero elements of the array at the same time.

Examples:

Input:
3
1 5 6
Output: 6
Operation 1: arr[] = {0, 4, 5}
Operation 2: arr[] = {0, 3, 4}
Operation 3: arr[] = {0, 2, 3}
Operation 4: arr[] = {0, 1, 2}
Operation 5: arr[] = {0, 0, 1}
Operation 6: arr[] = {0, 0, 0}

Input:2
1, 1
Output: 1
"""
def minSteps(arr, n):
    maxVal = max(arr) 
    return maxVal

n=int(input()) 
arr=list(map(int,input().split()))
print(minSteps(arr, n)) 
