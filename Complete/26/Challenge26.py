'''					Problem 26: Reciprocal Cycles

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

'''


primes = []

# Determine if number is prime
def isPrime(n):
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0 and n != i:
			return False
	return True

# Generate primes from 1-1000
for n in range(3, 1000, 2):
	if isPrime(n):
		primes.append(n)

# 2 and 5 are coprimes of 10 and will not return repeating decimals 
# and 2 was excluded from the beginning 
primes.remove(5)

# Determine period for repeating decimal for prime p 
def getCycle(p):
	mod = 0
	power = 1
	while mod != 1:
		mod = (10 ** power) % p 	
		power += 1

	return power - 1


longest_cycle = 0
num = 0

for prime in primes:
	cycle = getCycle(prime)
	if cycle > longest_cycle:
		longest_cycle = cycle
		num = prime

print("Number:", num, "Cycle:", longest_cycle)


