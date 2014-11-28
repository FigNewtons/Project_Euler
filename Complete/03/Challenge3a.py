#Input loop

ok = False
while not ok:
    numStr= input("Please enter a natural number: ")
    try:
        n= int(numStr)
        ok= True
        print("The prime factors of",numStr,"are: ")
    except ValueError:
        print("This is not a natural number.")
    
        



        

