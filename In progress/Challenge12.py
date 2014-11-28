#Project Euler Problem 12

numList = []


def triangle_gen():  
    n = 0
    x = 1
    while n>=0 and x<5000:
        n= n+x
        numList.append(n)
        x+=1
    else:
        return numList
    
numList= triangle_gen()

def divisor():
    for o, m in enumerate(numList):
        d = 1
        div = []
        while m>=d:
            if m%d==0:
                div.append(d)
                if len(div)>500:
                    print (m)
                    break
                else:
                    d+=1
            else:
                d+=1
divisor()             


                

            
        
    
    



    

        
            
        
