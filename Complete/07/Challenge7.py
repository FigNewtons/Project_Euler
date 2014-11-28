#Project Euler Challenge 7

#What is the 10,001st prime number?

def nth_prime(n):
    primes = [2]
    number = 3
    while len(primes)< n:
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
    return primes[n-1]

print(nth_prime(10001))
