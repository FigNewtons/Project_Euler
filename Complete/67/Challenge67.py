'''Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.'''

triangle = []

f = open("/home/nirvana/Desktop/triangle.txt") #change file path 

for line in f.readlines():
    line = line.split()  
    row = map(int, line)
    triangle.append(row)


#Most optimal path    
for row in range(99, 0 , -1):
    count = 0
    test = 0
    for n in triangle[row]:
        if count == 0:
            test = n
        elif n > test: 
            triangle[row - 1][count-1] += n
        else:
            triangle[row - 1][count-1] += test

	test = n
        count += 1

print(triangle[0][0])
    
