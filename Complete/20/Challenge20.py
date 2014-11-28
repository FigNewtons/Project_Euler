#Project Euler Challenge 20

#Find the sum of the digits in the number 100!

import math
m= math.factorial(100)
print(m)

n= sum(int(i) for i in str(m))
print (n)






