'''			Problem 27: Quadratic Primes

Find the product of the coefficients, a and b, for the below quadratic 
expression that produces the maximum number of primes for consecutive 
values of n, starting with n = 0.

n^2 + an + b , where |a| < 1000 and |b| < 1000

'''
import math 

# Generate primes
primes = [2,3,5,7]
def gen_primes():
	for n in range(9, 9999, 2):
		isPrime = True
		for divisor in range(3, int(math.sqrt(n)) + 1, 2):
			if n % divisor == 0:
				isPrime = False
				break
		if isPrime:
			primes.append(n)
		
# b must be a prime between 1-1000 
# else the equation won't return a prime 
# when n = 0

gen_primes()
b_range = primes[0:168]
primes = set(primes) # For O(1) lookup
# Represent count, product, a, and b respectively
values = [0,0,0,0] 

# Check for streaks
for a in range(-1000, 1000):
	for b in b_range:
		n = 0
		while True:
			if (n**2 + a * n + b) in primes:
				n += 1
			else: 
				break
		if n > values[0]:
			values = [n, a * b, a, b]

print("Max streak: " + str(values[0]) +
      "\nProduct: " + str(values[1]) +
	  "\na value: " + str(values[2]) +
	  "\nb value: " + str(values[3]))
 
	
			

	

