'''		Problem 25

What is the first term in the Fibonacci sequence to contain 1000 digits?

Paper and pencil solution:

phi = 1.618034 

You can calculate any Fibonacci number with the following formula:

phi^n / sqrt(5)		#Rounded to the nearest integer

Any number with 1000 digits is necesaarily greater than 10^999, thus:

phi^n / sqrt(5) > 10^999
n * log(phi) > 999 * log(10) + log(5)/2 
n > (999 * log(10) + log(5) / 2) / log(phi)
n = 4782

'''

f1, f2 = 1, 1
count = 2

while True:
	f1 += f2
	count += 1
	if(len(str(f1)) >= 1000):
		break

	f2 += f1
	count += 1
	if(len(str(f2)) >= 1000):
		break	
 
print(count)



