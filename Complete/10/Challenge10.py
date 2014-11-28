#Find the sum of all the primes below two million.

import math

n = 3
limit = 2000000

primes = [3]

while n < limit:
    isPrime = True
    for prime in primes:
	if n % prime == 0:
	    isPrime = False
	    break
        if prime > math.sqrt(n):
	    break
    if isPrime == True:
	primes.append(n)

    n += 2

primes.append(2)

print(sum(primes))




        
	
	    
	     
