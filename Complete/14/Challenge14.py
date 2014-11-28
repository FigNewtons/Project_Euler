'''		Problem 14: Longest Collatz Sequence
		
		Find which number under one million produces
		the longest collatz sequence.
'''

# Store past results of the collatz sequence to speed up calculations
sequence = {1: 1} 

def collatz(n, count):
	if n in sequence:
		return sequence[n] + count
	else:
		count += 1
		if n == 1:
			return count
		elif n % 2 == 0:
			return collatz(int(n/2), count)
		else:
			return collatz(3 * n + 1, count)


largest = 0
num = 1

for n in range(2, 1000000):
	sequence[n] = collatz(n, 0)
	if sequence[n] > largest:
		largest = sequence[n]
		num = n

print(num, largest)


