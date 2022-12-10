filename = 'input.txt'
message = ''

with open(filename, 'r') as f:
	message = f.read()

for i in range(len(message)-14):
	m = message[i:i+14]
	allLettersUnique = True

	for letter in m:
		if m.count(letter) > 1:
			allLettersUnique = False
			break

	if allLettersUnique:
		print(i+14)
		break
