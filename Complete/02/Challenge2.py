#Project Euler Challenge 2

#By considering the terms in the Fibonacci sequence
#whose values do not exceed four million, find the sum of the even-valued terms.

def fib (n):
   if n==1:
        return 1
   elif n==2:
        return 2
   else:
        return fib(n-1)+fib(n-2)

total=0
for n in range (1,33):
   if fib(n)%2==0:
      total +=fib(n)
print (total)
   
   
       
