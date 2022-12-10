filename = 'input.txt'
trees = []

with open(filename, 'r') as f:
	trees = f.read().split('\n')

trees = trees[:-1]

maxTreeScore = 0

for i in range(len(trees)):
	row = trees[i]
	for j in range(len(row)):
		treeHeight = int(row[j])
		
		treeLeftScore = 0
		for x in range(0, j):
			if (int(row[x]) >= treeHeight):
				treeLeftScore = 1
			else:
				treeLeftScore += 1

		treeRightScore = 0
		for x in range(j+1, len(row)):
			treeRightScore += 1
			if (int(row[x]) >= treeHeight):
				break

		treeUpScore = 0
		for y in range(0, i):
			if (int(trees[y][j]) >= treeHeight):
				treeUpScore = 1
			else:
				treeUpScore += 1

		treeDownScore = 0
		for y in range(i+1, len(trees)):
			treeDownScore += 1
			if (int(trees[y][j]) >= treeHeight):
				break

		treeScore = treeLeftScore * treeRightScore * treeUpScore * treeDownScore

		if (treeScore > maxTreeScore):
			maxTreeScore = treeScore

print(maxTreeScore)