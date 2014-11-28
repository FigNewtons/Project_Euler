''' Problem 12: Highly Divisible Triangular Number 

	What is the value of the first triangle number 
		to have over five hundred divisors?
'''
import math

primes = []

# Reads in list of prime numbers from another file into a list 
def getPrimes(file_path):
	fo = open(file_path)
	for line in fo:
		row = line.split()
		for n in row:
			primes.append(int(n))
	
#   Calculates the number of divisors
#	of a number based on its prime
#	factorization as follows:
#
#	Ex: 24 = 2^3 * 3^1
#
#	Take the exponents of its prime factors
#	(in this case 3 and 1), add 1 (4 and 2)
#	and return their product (8).

def numDivisors(num):
	divisors = 1
	for n in primes:
		count = 0
		if n > num:
			break
		else:
			while num % n == 0:
				num /= n
				count += 1

			divisors *= count + 1

	return divisors

# Gets the first triangle number with over 500 divisors (goal) 
# within a given range (limit)

def getTriangle(limit, goal):
	triangle = 0
	for n in range(1, limit):
		triangle += n
		div = numDivisors(triangle)
		if div > goal:
			return triangle

getPrimes("'/media/phoenix/Seagate Backup Plus Drive/Backup/Other/Python/Project Euler/Complete/12/primes.txt'")
print(getTriangle(100000, 500))
