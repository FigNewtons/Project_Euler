#Project Euler Challenge 9

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

m = 20
n = 1

while m>n:
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    if a+b+c == 1000:
        print (a*b*c)
        break
    elif a+b+c < 1000:
        n+=1
    elif a+b+c>1000 and m==n+1:
        m-=1
        n-=1
    elif a+b+c>1000:
        m-=1
