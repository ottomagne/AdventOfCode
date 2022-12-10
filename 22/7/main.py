filename = 'input.txt'
out = None
root = {}
cwd = '/'

with open(filename, 'r') as f:
	out = f.read().split('\n')

print(out)
out = out[1:-1] #already in / so no need for first cd, also strip last \n

for i in range(len(out)):
	line = out[i]
	if line[0] == "$":
		parts = line.split()
		command = parts[1]
		if command == "cd":
			# handle cd
		elif command == "ls":
			nextline = out[i+1]
			while (nextline[0] != '$' and i < len(out)):
				dirOrFileSize, name = nextline.split()
				if dirOrFileSize == 'dir':
					
