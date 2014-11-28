#How to filter out primes

composite = [ ]
for a in range (2,101):
    if a not in composite:
        n = a
        while (n*a <=101):
            composite.append (n*a)
            n+=1 
print (composite) 
