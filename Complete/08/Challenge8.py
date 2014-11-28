#Project Euler Challenge 8

#Part 1: Fetch url 
from urllib.request import urlopen 
page = urlopen("http://projecteuler.net/problem=8").read()
page = str(page)

#Part 2: Parse HTML

#2A: Remove outermost tags
info = [ ]    
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        info.append(data)

parser = MyHTMLParser(strict=False)
parser.feed(page)

#2B: Slice list to include just the numbers needed
number = info[84:123]

#2C: Remove all else surrounding the numbers 
numbers= [ ]
for i in number:
    if i== '<br />':
        number.remove(i)
        
for i in number:
    a, b = i.split('\\n',1)
    numbers.append(b)

#2D: Join to form one number 
number= ''.join(numbers)


#Part 3: Find greatest product of 5 consecutive numbers

#3A: Make list of digits in number
digits = [ ]
for ch in number:
    digits.append(ch)

#3B: Generate list of products
five = [ ]
products = [ ]
product = 1 
for i in digits:
    i = int(i)
    five.append(i)
    product = product*i
    while len(five)==5:
        products.append(product)
        f = five[0]
        if product>0:
            f = int(f)
            product = product/f 
            five.remove(f)
        elif product==0 and int(f)==0:
            a,b,c,d = int(five[1]),int(five[2]), int(five[3]), int(five[4])
            product = a*b*c*d
            five.remove(f)
        elif product==0 and int(f)!=0:
            five.remove(f)
            
#3C: Sort list and print last item for largest product
p = sorted(products)
print(p[-1])
    
    
    
    

