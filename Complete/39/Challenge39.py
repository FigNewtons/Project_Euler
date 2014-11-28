'''			Problem 39: Integer Right Triangles

For which value of p ≤ 1000, is the number of solutions maximised?

'''

perimeters = {}
for k in range(1,1001):
	perimeters[k] = 0

# Generate primitive pythagorean triples 
# Given 1 <= n < m,
#	a = m * n
#	b = (m^2 - n^2) / 2
#	c = (m^2 + n^2) / 2
#
# Given a perimeter p for a primitive pythagorean triple,
# there must be unique, derived triples with a perimeter n*p

for m in range(2, 100):
	for n in range(1, m - 1):
		if (m*m + n*n) % 2 == 0 and m*n % 2 != 0:
			p = (m * n) + int((m*m - n*n)/2) + int((m*m + n*n)/2)
			for p in range(p, 1000, p):
				perimeters[p] += 1


print(max(perimeters, key = perimeters.get))

