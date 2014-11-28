''' The total number of lattice paths in a grid of size a x b can be expressed as the binomial coefficient (a+b nCr a)-- this is because
the total number of possible paths is a combination. Thus, the total number of lattice paths for a 20 x 20 grid is 40 nCr 20.'''

import math

def nCr(n, k):
    num = math.factorial(n)
    denom = math.factorial(k) * math.factorial(n - k)
    print(num / denom) 


nCr(40,20)
