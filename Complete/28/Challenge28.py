'''What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Algorithm: One diagonal is formed by the squares of odd numbers. Thus, in a 5 x 5 grid, the upper-right hand
diagonal is 1, 9, and 25. For the remaining diagonals, just subtract n-1 from n^2 (where n is the odd number)
three times.

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

1  9 (Subtract n-1 or 2: 7, 5, 3) 25 (Subtract n-1 or 4: 21, 17, 13)

'''

total = 1

for n in range(3, 1002, 2):
    square = n * n
    diff = n - 1
    total += square
    count = 0
    while count < 3:
       square -= diff
       total += square
       count += 1

print(total)
