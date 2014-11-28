#Project Euler Challenge 5

#What is the smallest positive number that is
#evenly divisible by all of the numbers from 1 to 20?

#Part 1: Generate prime factors
factors = []
for n in range(2,21):
    divisor = 2
    while n>=divisor:
        if n%divisor==0:
            if divisor not in factors:
                factors.append(divisor)
                n=n/divisor
            else:
                n=n/divisor
        else:
            divisor+=1


#Part 2: Generate LCM
total = 1
for i in factors:
    max_lcd = 1
    while i<20:
        if i>max_lcd:
            max_lcd = i
            i = i*i
        else:
            i = i*i
    else:
        total = total * max_lcd
print(total)
            
