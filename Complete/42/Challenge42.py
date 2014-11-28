'''				Problem 42: Coded Triangle Numbers

		How many common English words are triangle words?

'''
import string
import math 

file_path = "words.txt"

fo = open(file_path)

for word in fo:
	word = word.replace(',','')
	word = word.replace('"',' ')
	word = word.split()

# Create dictionary for uppercase value letters A-1, B-2, C-3, etc.
alpha = string.ascii_uppercase
value = {}
for val, letter in enumerate(alpha):
	value[letter] = val + 1


def inv_tri(x):
	return (math.sqrt(8 * x + 1) - 1) / 2	

total = 0
for w in word:
	w_val = 0
	for letter in w:
		w_val += value[letter]

	if inv_tri(w_val) % 1 == 0:
		total += 1

print(total)
