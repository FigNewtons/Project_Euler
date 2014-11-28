#Test for prime factors

numStr= input("Please enter a natural number: ")
n= int(numStr)                                      #Input number
a = 1

if n==1 or n==0:
    print ("Ignore")    
else:
    while (a<n):
        a+=1
        while n%a==0:
            print (a)
            n=n/a
        



    

        
        
        
        
        

            

           
           
