#Project Euler Challenge 17

#If all the numbers from 1 to 1000 (one thousand)
#inclusive were written out in words, how many letters would be used?

#Part 1: Make list of words used
ones= ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten','eleven','twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen','eighteen','nineteen']
tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
hundreds= ['hundred']
thousands=['thousand']

#Part 2: Get list of word length from each list

ones_length=[]
teens_length=[]
tens_length=[]
hundreds_length=[]
thousands_length=[]


# 2A: Function to generate word length
def get_length(list_word, list_length):
    for a in list_word:
        b = len(a)
        list_length.append(b)


get_length(ones, ones_length)
get_length(teens, teens_length)
get_length(tens, tens_length)
get_length(hundreds, hundreds_length)
get_length(thousands, thousands_length)



#Part 3: Calculate total
real_grand_total=[]
grand_total = []

def get_total1(list_length):
    total = 0
    for n in list_length:
        total += n
    grand_total.append(total)

    
get_total1(ones_length)  #1-9
get_total1(teens_length) #10-19

def get_total2(list_length1, list_length2):
    total = 0
    for m in list_length1:
        total += m
        for n in list_length2:
            a = m + n
            total += a
    grand_total.append(total)

get_total2(tens_length, ones_length)#20-99

cohundreds=[]
def get_total3(list_length1, list_length2,list_length3):
    total = 0
    for m in list_length1:
        for n in list_length2:
            a = m + n
            cohundreds.append(a)
            total += a
    b = list_length1[0]+list_length3[0]
    total += b
    real_grand_total.append(total)

get_total3(ones_length, hundreds_length, thousands_length)#100,200,300,400,500,600,700,800,900,1000

def get_total4(grand, colist):
    total = 0
    cumulative_total = 0
    for m in grand:
        total += m   #1-99 total
    real_grand_total.append(total)
    for n in colist:
         o = (n * 99) + (3*99)+ total # ex: onehundred + and + one 
         cumulative_total +=o
    real_grand_total.append(cumulative_total)
    
get_total4(grand_total, cohundreds)
        
final = 0        
for i in real_grand_total:
    final += i
print(final)
