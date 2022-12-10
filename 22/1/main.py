filename = 'input.txt'
elves = None
totals = []
three = 0

with open(filename, 'r') as f:
    elves = f.read().split('\n\n')
elves[-1] = elves[-1].strip()
for e in elves:
	calories = e.split('\n')
	totals.append(sum([int(c) for c in calories]))

for i in range(3):
	three += max(totals)
	totals.remove(max(totals))
print(three)
