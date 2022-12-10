from itertools import zip_longest

filename = 'input.txt'
rucks = None
prioritySum = 0

with open(filename, 'r') as f:
	rucks = f.readlines()

groups = [rucks[n:n+3] for n in range(0, len(rucks), 3)]

for group in groups:
	for ruck in group:
		ruck = ruck.strip()
	for letter in group[0]:
		if letter in group[1] and letter in group[2]:
			prioritySum += ord(letter) - 38 if letter.isupper() else ord(letter) - 96
			break
print(prioritySum)