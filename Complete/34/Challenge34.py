'''Project Euler Challenge 34

Find the sum of all numbers which are
equal to the sum of the factorial of their digits.
'''
#Part 1: Generate factorials for digits 1-9
import math 
factorial = [ ]
for i in range(0,10):
    i = math.factorial(i)
    factorial.append(i)


#Part 2: Generate numbers
sum_fact = 0
total = 0
for n in range(3,999999):
    a = str(n)
    length = 0
    for ch in a:
        b = int(ch)
        total = total + int(factorial[b])
        length +=1
        if total == n and length==len(a):
            sum_fact = sum_fact + n
        elif total !=n and length==len(a):
            total = 0

print(sum_fact)
        
