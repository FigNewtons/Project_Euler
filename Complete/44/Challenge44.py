'''				Problem 44: Pentagon Numbers

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference 
	are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

'''
import math

def pentagon(n):
	return n * (3 * n - 1 ) / 2

def pentInv(x):
	return (math.sqrt(24 * x + 1) + 1)/ 6.0


# Store pentagon numbers in list
pent_num = [] 

for n in range(1,100000):
	pent_num.append(int(pentagon(n)))

# Search using inverse function 
found = False
m = 2
while not found:
	for n in range(m - 1, 0, -1):       
		add = pent_num[m] + pent_num[n]
		diff = pent_num[m] - pent_num[n]
		if pentInv(add) % 1 == 0 and pentInv(diff) % 1 == 0:	
			print(diff)
			found = True
	
	m += 1






