"""
Given a matrix mat[][] of size mXn, pair of indices X and Y, the task is to find the number of moves to bring all 

the non-zero elements of the matrix to the given cell at (X, Y). 

Note: A move consists of moving an element at any cell to its four directional adjacent cells i.e., left, right, top, bottom. 
 
Input:
First line contains integer m and integer n
Next m lines contains row elements of matrix
Next line contains integr x and integer y

Output:
Print the minimum moves required
Examples: 
Input:
2 2
1 0
1 0
1 1
Output:
3 
Explanation: 
Moves required => 
For Index (0, 0) => 2 
For Index (1, 0) => 1 
Total moves required = 3
Input:
3 4
1 0 1 0
1 1 0 1
0 0 1 0
1 3
Output: 
13
Input:
1 1
2
0 0
Output:
0
Input:
3 3
1 2 3
4 5 6
6 7 8
2 2
Output:
18
Input:
3 3
1 2 3
1 2 3
1 2 3
1 1
Output:
12
"""
M,N=map(int,input().split())
l=[]
def no_of_moves(Matrix, x, y):
    moves = 0
    for i in range(M): 
        for j in range(N):
            if (Matrix[i][j] != 0): 
                moves += abs(x - i) 
                moves += abs(y - j) 
  
    print(moves)
for i in range(M):
    l.append(list(map(int,input().split())))
x,y=map(int,input().split())
no_of_moves(l, x, y)
