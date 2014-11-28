#Project Euler Challenge 10

#Find the sum of all the primes below two million.

def prime_limit(n):
    primes = [2]
    number = 3
    a = primes[-1]
    while a < n:
        isPrime = True
        for prime in primes:
            if number%prime==0:
                isPrime= False
                break
            if (prime * prime > number):
                break
        if isPrime:
            primes.append(number)
        number += 2
    total = 0
    for i in primes:
        total += i
    print(total)   
prime_limit(2000000)

