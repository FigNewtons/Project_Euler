#Project Euler Challenge 24

#What is the millionth lexicographic
#permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import itertools

lex = [ ]
for perm in itertools.permutations([0,1,2,3,4,5,6,7,8,9],10):
    lex.append(perm)

print (lex[999999])
    





