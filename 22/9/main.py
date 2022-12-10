class Rope:
	def __init__(self):
		self.knots = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		self.tailPositions = {(0,0)}

	def move(self, direction, moves):
		for i in range(moves):
			headx, heady = self.knots[0]
			#print(f'before: head: {self.knots[0]}')
			if direction == "R":
				self.knots[0] = (headx+1, heady)
			elif direction == "L":
				self.knots[0] = (headx-1, heady)
			elif direction == "U":
				self.knots[0] = (headx, heady-1)
			elif direction == "D":
				self.knots[0] = (headx, heady+1)
			#print(f'after: head: {self.knots[0]}')

			for i in range(1, len(self.knots)):
				#print(f'before: knot {i}: {self.knots[i]}')
				self.moveTail(i)
				#print(f'after: knot {i}: {self.knots[i]}')

			#add current tail position to set
			self.tailPositions.add(self.knots[len(self.knots)-1])
			#print()

	def moveTail(self, knotToMoveIndex):
		headx, heady = self.knots[knotToMoveIndex-1]
		tailx, taily = self.knots[knotToMoveIndex]

		deltaX = headx-tailx
		deltaY = heady-taily
		#check to make sure the tail needs to be moved in general
		if (abs(deltaX) > 1 or abs(deltaY) > 1):

			#if the previous knot moved on two axes, this one will also move on both axes
			if abs(deltaX) > 1 and abs(deltaY) > 1:
				tailx += deltaX - (1 if deltaX > 0 else -1)
				taily += deltaY - (1 if deltaY > 0 else -1)

			#otherwise, if the previous knot is diagonal but moved on one axis, this one will move diagonal 
			elif abs(deltaX) > 1 and abs(deltaY):
				tailx += deltaX - (1 if deltaX > 0 else -1)
				taily += deltaY
			elif abs(deltaX) and abs(deltaY) > 1:
				tailx += deltaX
				taily += deltaY - (1 if deltaY > 0 else -1)

			#otherwise, the knot is following a knot purely along one axis
			elif abs(deltaX) > 1:
				tailx += deltaX - (1 if deltaX > 0 else -1)

			elif abs(deltaY) > 1:
				taily += deltaY - (1 if deltaY > 0 else -1)

			self.knots[knotToMoveIndex] = (tailx, taily)


filename = 'input.txt'
instructions = None
r = Rope()

with open(filename, 'r') as f:
	instructions = f.read().split('\n')

instructions = instructions[:-1]

for instruction in instructions:
	direction, moves = instruction.split()
	r.move(direction, int(moves))


print(len(r.tailPositions))