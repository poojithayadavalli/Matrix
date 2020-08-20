
"""
Given a NxM matrix of integers containing duplicate elements. 

The task is to find the sum of all even occurring elements in the given matrix.

That is the sum of all such elements whose frequency is even in the matrix.

Input:
Firstline indicates integer N and integer M
Next N lines contains elements of matrix.
Output:
print sum of all elements with even frequency

Examples:

Input :
3 3
1 1 2
2 3 3
4 5 3
Output :
6
The even occurring elements are 1,2 and they 
occurs only 2 times.
Therefore, sum = 1*2+2*2 = 6

Input :
2 2
10 20
40 40
Output : 
80
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
2
"""
M,N=map(int,input().split())
def sumOddOccuring(arr):
    mp = dict() 
    for i in range(N): 
        for j in range(M): 
            if arr[i][j] in mp: 
                mp[arr[i][j]] += 1
            else: 
                mp[arr[i][j]] = 1
    s = 0
    for i in mp: 
        if mp[i] % 2 == 0: 
            x = mp[i] 
            s += i * mp[i] 
  
    return s 
mat=[]
for i in range(M):
    mat.append(list(map(int,input().split())))
print(sumOddOccuring(mat))


