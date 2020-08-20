"""
Given an array arr[] of N elements, the task is to find the product of the elements which have prime frequencies in the array.

Since, the product can be large so print the product modulo 109 + 7. Note that 1 is neither prime nor composite.

Examples:

Input:
6
5 4 6 5 4 6
Output: 
120
All the elements appear 2 times which is a prime
So, 5 * 4 * 6 = 120

Input:
9
1 2 3 3 2 3 2 3 3
Output: 6
Only 2 and 3 appears prime number of times i.e. 3 and 5 respectively.
So, 2 * 3 = 6

Input:
5
1 1 2 2 3
Output:
2
Input:
5
2 2 2 3 3
Output:
6
Input:
6
1 2 2 2 2 1
output:
1
"""
MOD = 1000000007
def SieveOfEratosthenes(prime, p_size):
    prime[0] = False
    prime[1] = False
  
    for p in range(2, p_size):
        if (prime[p]):
            for i in range(2 * p, p_size, p): 
                prime[i] = False
 
def productPrimeFreq(arr, n): 
    prime = [True for i in range(n + 1)]
    SieveOfEratosthenes(prime, n + 1)
    i, j = 0, 0 
    m = dict() 
    for i in range(n): 
        m[arr[i]] = m.get(arr[i], 0) + 1
    product = 1
    for it in m:
        if (prime[m[it]]): 
            product *= it % MOD 
            product %= MOD
    return product
n=int(input())
arr = list(map(int,input().split())) 
print(productPrimeFreq(arr, n))
