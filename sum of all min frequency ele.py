"""
Given a NxM matrix of integers containing duplicate elements. 
The task is to find the sum of all minimum occurring elements in the given matrix.
That is the sum of all such elements whose frequency is minimum in the matrix.

Input:
Firstline indicates integer N and integer M
Next N lines contains elements of matrix.
Output:
print sum of all elements with min frequency

Examples:

Input :
3 3
1 1 2
2 3 3
4 5 3
Output : 
9
The even occurring elements are 4,5 and their number
of occurrences are 1,1 respectively. Therefore,
sum = 4+5 = 9.

Input :
2 2
10 20
40 40
Output : 
30
Input:
4 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
Output:
40
Input:
2 2
1 2
2 3
Output:
4
Input:
2 2
1 1
2 3
Output:
5
"""
import sys
def sumMinOccuring(mat): 
    n,m=len(mat),len(mat[0]) 
    _map={} 
    for i in range(n): 
        for j in range(m): 
            d=mat[i][j] 
            if d in _map: 
                _map[d]=_map.get(d)+1
            else: 
                _map[d]=1
    _sum,minFreq=0,sys.maxsize 
    for i in _map: 
        minFreq=min(minFreq,_map.get(i))
    for i in range(n): 
        for j in range(m): 
            if _map.get(mat[i][j])==minFreq: 
                _sum+=mat[i][j] 
      
    return _sum 
n,m=map(int,input().split())
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
print(sumMinOccuring(mat))
