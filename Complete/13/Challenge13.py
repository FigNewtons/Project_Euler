#Project Euler Challenge 13

#Part 1: Fetch Url
from urllib.request import urlopen 
page = urlopen("http://projecteuler.net/problem=13").read()
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
number = info[84:-168]

#2C: Remove all else surrounding the numbers 
numbers= [ ]
for i in number:
    if i== '<br />':
        number.remove(i)
        
for i in number:
    a, b = i.split('\\n',1)
    numbers.append(b)


#Part 3: Find the sum of the digits
total = 0
for i in numbers:
    i = int(i)
    total = total + i
    
#Part 4: Print first 10 digits of sum
digits = []
total = str(total)
for ch in total:
    digits.append(ch)

print(digits[:10])
