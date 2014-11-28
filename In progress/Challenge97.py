'''Project Euler Challenge 97

However, in 2004 there was found a massive
non-Mersenne prime which contains 2,357,207 digits: 28433×2^(7830457)+1.

Find the last ten digits of this prime number.'''

'''import timeit


t = timeit.Timer(stmt = "(8**20) % 2")
print (t.timeit())

t = timeit.Timer(stmt = "pow(8,20,2)")
print (t.timeit())'''


def PE97(a, b, c, m):
    return (c * pow(a, b, 10**m) + 1) % 10**m
print ("Answer to PE97 = ",  PE97(2, 7830457, 28433, 10))



