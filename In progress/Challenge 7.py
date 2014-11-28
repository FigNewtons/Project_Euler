#Project Euler Challenge 7

composite = [ ]
prime = [ ]
for a in range (2,101):
    if a not in composite:
        n = a
        while (n*a <=101):
            composite.append (n*a)
            n+=1

            
for b in range (2,101):
    if b not in composite:
        prime.append (b)

print (prime[10]) 



    


          
        
        
        
    
        
