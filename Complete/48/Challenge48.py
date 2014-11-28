#Project Euler Challenge 48

#Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

total = 0
for i in range(1,1001):
    total = total + (i**i)

s = str(total)
n = s[-10:]
print(n)
