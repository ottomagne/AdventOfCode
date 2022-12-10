filename = 'input.txt'
data = ''
stacks = []

with open(filename, 'r') as f:
	data = f.read()

boxs, instructions = data.split('\n\n')

numStacks = boxs.strip()[-1]

for i in range(int(numStacks)):
	stacks.append([])


lines = boxs.split('\n')[:-1]

for i in range(len(lines)):
	line = lines[-i-1]
	items = [line[i:i+3] for i in range(0, len(line), 4)]
	for j in range(len(items)):
		item = items[j]
		if item == '   ':
			continue
		else:
			item = item[1]
		stacks[j].append(item)

instructions = instructions.strip().split('\n')


for instruction in instructions:
	words = instruction.split()
	howMany = int(words[1])
	fromWhere = int(words[3]) - 1
	toWhere = int(words[5]) - 1
	tempStack = []

	for i in range(howMany):
		tempStack.append(stacks[fromWhere].pop())
	
	for i in range(howMany):
		stacks[toWhere].append(tempStack.pop())

for stack in stacks:
	print(stack[-1], end='')