'''				Problem 36: Double-base Palindromes

The decimal number, 585 = 10010010012 (binary), is palindromic 
in both bases.

Find the sum of all numbers, less than one million, which are 
palindromic in base 10 and base 2.

(No leading zeros!)
'''

'''
Note: No even number will be a palindrome in binary.
This is because the 2^0 place will always be zero while
the leading digit must always be one. 

1xxxxxx0 
'''

# Returns true if num is a palindrome in its given base
def is_palindrome(num):
	forward = str(num)	
	backward = forward[::-1]
	return forward == backward

# Check if n is a palindrome in both base 10 and base 2
total = 0
for n in range(1, 1000000, 2):
	if is_palindrome(n) and is_palindrome(bin(n)[2:]):
		total += n

print(total)



