filename = 'input.txt'
ids = None
numContained = 0

with open(filename, 'r') as f:
	ids = f.readlines()

for pair in ids:
	pair = pair.strip()
	a, b = pair.split(',')
	aMin, aMax = [int(x) for x in a.split('-')]
	bMin, bMax = [int(x) for x in b.split('-')]
	overlap = False
	if ((bMin <= aMax and bMax >= aMax) or (aMin <= bMax and aMax >= bMax)):
		numContained += 1
		overlap = True
	print(f'aMin: {aMin}, aMax: {aMax}, bMin: {bMin}, bMax: {bMax} OVERLAP: {overlap}')

print(numContained)