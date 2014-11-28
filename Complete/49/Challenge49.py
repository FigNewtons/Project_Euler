'''			Problem 49: Prime Permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

'''

import math, itertools

# Returns true if the number is prime (only feed in odd numbers!)
def is_prime(num):
	for divisor in range(3, int(math.sqrt(num) + 1)):
		if num % divisor == 0:
			return False
	return True

# Prepare list of 4-digit prime numbers
primes = []
for m in range(1001, 9999, 2):
	if is_prime(m):
		primes.append(m)

# Returns true if three numbers are permutations of each other
def is_perm(num1, num2, num3):
	num1 = [s for s in str(num1)]
	num2 = [s for s in str(num2)]
	num3 = [s for s in str(num3)]
	return sorted(num1) == sorted(num2) == sorted(num3)

# Check for the prime permuations 
check = set(primes)
for prime in primes:
	for n in range(2, 4498, 2):
		 # Create triplet offset by equal amount 
		group = [prime, prime+n, prime+(2*n)]
		if group[1] > 10000 or group[2] > 10000:
			continue
		elif group[1] in check and group[2] in check:
			if is_perm(group[0], group[1], group[2]):
				print(group, str(group[0]) + str(group[1]) + str(group[2]))
	

	

