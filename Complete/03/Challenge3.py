#Project Euler Challenge 3

#What is the largest prime factor of the number 600851475143?

ok = False
while not ok:
    numStr= input("Please enter a natural number: ")
    try:
        n= int(numStr)
        a = 1
        ok= True
        if n==1 or n==0:
            print("The prime factors of",numStr,"are: none. This number is neither prime or composite.")
        else:
            print("The prime factors of",numStr,"are: ")
            while (a<n):
                a+=1
                while n%a==0:
                    print (a)
                    n=n/a 
    except ValueError:
        print("This is not a natural number.")
    
        



        

