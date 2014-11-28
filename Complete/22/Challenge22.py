''' 				Problem 22: Names Scores

		What is the total of all the name scores in the file?

'''
import string

# Parse and sort list of names 
file_path = "'/media/phoenix/Seagate Backup Plus Drive/Backup/Other/Python/Project Euler/Complete/22- Incomplete/names.txt'"

fo = open(file_path)

for line in fo:
	line = line.replace(',','')
	line = line.replace('"',' ')
	line = line.split()

line = sorted(line)


# Create dictionary for uppercase value letters A-1, B-2, C-3, etc.
alpha = string.ascii_uppercase
value = {}
for val, letter in enumerate(alpha):
	value[letter] = val + 1


# Get total score
total = 0
for pos, name in enumerate(line):
	name_score = 0
	for letter in name:
		 name_score += value[letter]

	name_score *= pos + 1
	total += name_score

print(total)
