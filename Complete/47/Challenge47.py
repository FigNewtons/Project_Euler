'''		Project Euler
		Problem 47: Distinct Prime Factors

		Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''

def gen_primes(n):
	sieve = [True] * n
	for i in range(3, int(n ** 0.5) + 1 , 2):
		if sieve[i]:
			sieve[i * i :: 2 * i] = [False]* int((n-i*i-1)/(2*i)+1)
	return [2] + [i for i in range(3, n, 2) if sieve[i]]


def factor(n):
	count = []
	index = 0
	while n not in prime_set and n != 1:
		if n % primes[index] == 0:
			if primes[index] not in count:
				count.append(primes[index])
			n = n / primes[index]
		else:
			index += 1
	count.append(int(n))

	return len(count) 
	

primes = gen_primes(10000000)
prime_set = set(primes)

four_count = 0
for num in range(210, 10000000, 1):
	if num not in prime_set:
		prime_count = factor(num)
		if prime_count == 4:
			four_count += 1
			if four_count == 4:
				print(num - 3)
				break		
		else:
			four_count = 0
	else:
		four_count = 0


		



	








