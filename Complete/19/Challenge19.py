'''				Problem 19: Counting Sundays

		How many Sundays fell on the first of the month during 
		the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

# 31 days - 3 day shift to right
# 30 days - 2 day shift to right
# 29 days - 1 day shift to right 
# 28 days - no change
month_change = [3,0,3,2,3,2,3,3,2,3,2,3]


# Sun - 0 , Mon - 1, Tues - 2, etc.
days = { 0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}

# Count how many Sundays are first of the month 
count = 0

# Computes the day of the week the following New Year's falls on
def newYear(start_day, leap):
	first = start_day	
	global count 

	for month in month_change:
		# Check for leap year 
		if month == 0 and leap:
			first = (first + month + 1) % 7
		else:
			first = (first + month) % 7

		if first == 0:
			count += 1

	return first


# January 1, 1901 was a Tuesday
start_day = 2

for year in range(1901, 2001):
	if year % 4 == 0:
		leap = True
	else:
		leap = False

	start_day = newYear(start_day, leap)

print(count)





