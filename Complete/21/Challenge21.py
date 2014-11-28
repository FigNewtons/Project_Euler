'''			Problem 21

Evaluate the sum of all the amicable numbers under 10000

'''

amicable = [0, 0]

'''Modified divisor generator -- since m isn't 
part of the sum we start the range at 2 and initialize
total to 1'''

for m in range(2, 10000):
	total = 1
	for n in range(2, int(m**0.5)+1):
		if m % n == 0:
			total = total + n + int(m/n)
	amicable.append(total)


answer = 0 
for m, total in enumerate(amicable):
	if m == 0 or m == 1 or total > 10000:
		continue
	if m == amicable[total] and m != total:
		answer += m

print(answer)




