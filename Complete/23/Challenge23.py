'''			Problem 23

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

'''

abundant_nums = []

for m in range(12, 21824):
	total = 1
	for n in range(2, int(m**0.5)+1):
		if m % n == 0:
			total = total + n + int(m/n)
			if n == int(m/n):
				total -= n
	if total > m:
		abundant_nums.append(m)


r = [n for n in range(1, 21823)]

sums = []
for num in abundant_nums:
	for num2 in abundant_nums:
		if num + num2 < 21823:
			sums.append(num + num2)

print(sum(set(r).difference(set(sums))))

