"""
Given an array of integers arr[] of size N, the task is to count all the elements of the array which have a frequency equals to its value.

Constraints:
1<=N<=1000

Input:
First line contains integer N
Second line contains the elements of array
Output:
Print the count of elements that satisfy given condition.

Examples:

Input:
6
3 2 2 3 4 3
Output: 2
Frequency of element 2 is 2
Frequency of element 3 is 3
Frequency of element 4 is 1
2 and 3 are elements which have same frequency as it’s value

Input:
6
1 2 3 4 5 6
Output: 1

Input:
4
1 2 2 3
Output:
2
Input:
3
1 2 3
Output:
1
Input:
5
2 3 3 3 4
Output:
1
"""
n=int(input())
arr=list(map(int,input().split()))
def findm(arr,n):
    mp={}
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1
    ans=0
    for i,j in mp.items():
        if i==j:
            ans+=1
    return ans
print(findm(arr,n))
