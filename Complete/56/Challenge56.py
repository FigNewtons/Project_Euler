'''				Problem 56: Powerful digit sum

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, 
what is the maximum digital sum?

'''

value = {'0':0 , '1':1, '2':2, '3':3, '4':4, 
'5':5, '6':6, '7':7, '8':8, '9':9}

# Returns the digit sum of the number
def digit_sum(num):
	total = 0
	for digit in str(num):
		total += value[digit]
	return total


# I assumed the max digit sum would be where
# a and b were between 90 and 100, since this range
# balances out the length of the number vs the possibility
# that a shorter number has higher individual digits and thus
# a larger overall sum
max_sum = 0
for a in range(90,100):
	for b in range(90, 100):
		ds = digit_sum(a**b)
		if ds > max_sum:
			max_sum = ds

print(max_sum)	
	

	
	
