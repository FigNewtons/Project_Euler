'''				Problem 35: Circular Primes

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''

import math 

# Generate primes
primes = [2,3,5,7]
def gen_primes():
	for n in range(9, 1000000, 2):
		isPrime = True
		for divisor in range(3, int(math.sqrt(n)) + 1, 2):
			if n % divisor == 0:
				isPrime = False
				break
		if isPrime:
			primes.append(n)

# Cycles through digits of num 
# and returns true if each rotation
# is also prime
def is_circular(num):
	for n in range(len(num) - 1):
		num = num[1:] + num[0]
		if int(num) not in p_set:
			return False
	return True 


gen_primes()
p_set = set(primes)

# Count number of circular primes
count = 0
for prime in primes:
	string = str(prime)
	if len(string) == 1 or is_circular(string):
		count += 1
	

print(count)

'''
At the moment, this code is SLOW! 

Note: All circular primes must only contain the digits 1,3,7,9
If not, one of its rotations will end in an even number or 5, 
and thus will not be prime. 

# Checks if each digit is either a
# 1,3,7 or 9 and returns false otherwise.
def check_digits(num):
	for digit in num:
		if digit in '24568':
			return False
	return True

'''


		
