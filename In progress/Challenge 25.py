#Project Euler 25

#What is the first term in the Fibonacci sequence to contain 1000 digits?

def fib (n):
   if n==1:
      return 1
   elif n==2:
      return 1
   elif n==3:
      return 2
   else:
        return fib(n-1)+fib(n-2)

for n in range(1,1000):
   s = fib(n)
   t = str(s)
   if len(t)==1000:
      print(n)
      break
    
