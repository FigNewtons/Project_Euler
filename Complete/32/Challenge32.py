'''			Problem 32: Pandigital Products

We shall say that an n-digit number is pandigital if it makes 
use of all the digits 1 to n exactly once. Find the sum of all 
products whose multiplicand/multiplier/product identity can be 
written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so 
be sure to only include it once in your sum.
'''

# The only way to achieve this is to multiply a 2-digit number
# by a three digit number or a 1-digit by a 4-digit number
# to get a four digit number.


# Returns true if a number contains the digit 0
def has_zero(num):
	for d in str(num):
		if d == '0':
			return True
	return False

# Returns true if the three numbers are 1-9 pandigital
def is_pandigital(m, n, product):
	digit = set(['1','2','3','4','5','6','7','8','9'])
	test = set(str(m) + str(n) + str(product))
	return sorted(digit) == sorted(test)

# Returns true if the three numbers contain 9 digits between them
def has_length_9(m,n,product):
	length = len(str(m)) + len(str(n)) + len(str(product))
	return 9 == length

# Finds the pandigital triples 
# (I could've optimized the for loops better, but whatever)
pandigital = []
for m in range(2, 100):
	if has_zero(m):
		continue
	for n in range(10000,100, -1):
		if has_zero(n):
			continue
		product = m * n
		if has_length_9(m,n,product) and is_pandigital(m,n,product):
			pandigital.append(product)
			

total = sum(set(pandigital))
print(total)







