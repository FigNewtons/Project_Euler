'''			Project Euler
			Problem 97: Large non-Mersenne Prime

In 2004 there was found a massive non-Mersenne prime 
which contains 2,357,207 digits: 28433 × 2^7830457 + 1.

Find the last ten digits of this prime number.

'''

# This is the quicker way

# You take the binary representation of the exponent to determine how 
# to decompose the number in less operations. For example, say we want to 
# compute 2**17. In binary 17 = 10001, or 2**4 + 2**1. This means that
# 2**17 = 2**(2**4 + 2**1) = 2**(2**4) * 2**(2**1) by the rules of exponents.

exp = str(bin(7830457))
exp = exp[2:]

base = 1
for num, val in enumerate(exp):
	if int(val) == 1:
		e = 2 ** (2 ** (len(exp) - 1 - num)) % 10000000000
		base = base * e % 10000000000

prime = 28433 * base % 10000000000 
prime = prime + 1

print(prime)	


'''
# This is the slow but straightforward way
base = 1
for i in range(0, 7830457):
	base = 2 * base % 10000000000	

prime = 28433 * base % 10000000000 
prime = prime + 1

print(prime)
'''
