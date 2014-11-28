#Project Euler Challenge 4

#Find the largest palindrome made from the product of two 3-digit numbers.

a = 999
b = 999
palindrome = [ ]

while a>=100 and b>=100:
    product = a*b
    if str(product)== str(product)[::-1]:
        palindrome.append(product)
        b -=1
    else:
        if a>=b and b>=101:
            b-=1
        elif b==100:
            a-=1
            b = a
palindrome.sort()
print(palindrome[-1])
    
