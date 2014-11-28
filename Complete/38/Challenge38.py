'''			Problem 38: Pandigital Multiples

What is the largest 1 to 9 pandigital 9-digit number that 
can be formed as the concatenated product of an integer 
with (1,2, ... , n) where n > 1?

'''

# Returns true if a number contains the digit 0
def has_zero(num):
	for d in str(num):
		if d == '0':
			return True
	return False

# Returns true if the list of numbers are 1-9 pandigital
def is_pandigital(products):
	digit = set(['1','2','3','4','5','6','7','8','9'])
	test = []
	for product in products:
		for d in str(product):
			test.append(d)
	test = set(test)
	return sorted(digit) == sorted(test)

# Returns the number of digits total
def num_digits(products):
	length = 0
	for product in products:
		length += len(str(product))
	return length

# Retruns a concatenated string of the products
def concat(products):
	return ''.join(str(s) for s in products)

# Find the largest pandigital number
largest_pan = 0
for num in range(1, 9999):
	products = []
	n = 1
	while num_digits(products) < 9: 
		products.append(num * n)
		n += 1
	if num_digits(products) == 9:
		result = int(concat(products))
		if is_pandigital(products) and result > largest_pan:
			largest_pan = result

print(largest_pan)

