'''				Problem 30: Digit Fifth Powers

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

'''
import math

# Store fifth powers 
fifth_powers = []
for n in range(0,10):
	fifth_powers.append(int(math.pow(n, 5)))


grand_total = 0
for i in range(10, 1000001):
	num = str(i)
	total = 0
	for j in range(len(num)):
		total += fifth_powers[int(num[j])]

	if total == i:
		grand_total += i

print(grand_total)
