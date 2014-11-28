'''		Project Euler
		Problem 52: Permuted Multiples
	
		Find the smallest positive integer, x, such that 
		2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

import collections

# Compare multisets -- sets that contain duplicate values
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

found = False
num = 2
while not found:
	str_num = sorted(str(num))
	
	for i in range(2, 7):
		times = sorted(str(num * i))
		if not compare(str_num, times):
			break
		elif i == 6:
			print(num)
			found = True

	num += 1

	


