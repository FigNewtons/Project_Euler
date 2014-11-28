#Project Euler Challenge 21

'''
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b
are an amicable pair and each of a and b are called amicable numbers.
Evaluate the sum of all the amicable numbers under 10000.
'''
 
#Part 1: Get sum of divisors
divisors_sum = []

def divisor_sum(n):
    divisor_sum = 0
    divisor = []
    counter = 1
    while counter<=n:
        if n%counter==0:
            divisor.append(counter)
            counter +=1
        else:
            counter +=1
    for i in divisor:
        divisor_sum += i
    divisors_sum.append(divisor_sum)


#Part 2: Generate integers under 10000 and call within function

for n in range(10000):
    divisor_sum(n)

#Part 3: Check for amicable pairs
total = 0
for n in range(10000):
    a= int(divisors_sum[n-1])
    if n<10000 and a<10000 and a!=n:
        if n == int(divisors_sum[a-1]):
            b = n + a
            total += b


print(total)
        
   
    


        
