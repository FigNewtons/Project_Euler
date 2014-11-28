#Project Euler Challenge 6

#Find the difference between the sum of the squares of the
#first one hundred natural numbers and the square of the sum.

sheep=0
dolly=0
total=0
for n in range (1,101):
    a=n**2
    sheep+=n           #sheep is the sum from 1 to 10
    daisy=sheep**2     #daisy is square of sum
    dolly+=a           #dolly is sum of squares
total= daisy-dolly
print (total)

    
    
    
