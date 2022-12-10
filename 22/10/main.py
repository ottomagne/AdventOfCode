filename = 'input.txt'

def calculateSignalStrength(ops, cycleNum):
	reg = 1
	insPtr = 0
	processingAdd = False

	for i in range(cycleNum-1):
		splitOp = ops[insPtr].split()
		if splitOp[0] != "noop":
			if processingAdd:
				processingAdd = False
				reg += int(splitOp[1])
				insPtr += 1
			else:
				processingAdd = True
		else:
			insPtr += 1

	return cycleNum*reg

ops = None
with open(filename, 'r') as f:
	ops = f.read().split('\n')[:-1]

sigStrength20  = calculateSignalStrength(ops, 20)
sigStrength60  = calculateSignalStrength(ops, 60)
sigStrength100 = calculateSignalStrength(ops, 100)
sigStrength140 = calculateSignalStrength(ops, 140)
sigStrength180 = calculateSignalStrength(ops, 180)
sigStrength220 = calculateSignalStrength(ops, 220)

print(f'20th Cycle Strength: {sigStrength20}')
print(f'60th Cycle Strength: {sigStrength60}')
print(f'100th Cycle Strength: {sigStrength100}')
print(f'140th Cycle Strength: {sigStrength140}')
print(f'180th Cycle Strength: {sigStrength180}')
print(f'220th Cycle Strength: {sigStrength220}')

print(f'Total: {sigStrength20+sigStrength60+sigStrength100+sigStrength140+sigStrength180+sigStrength220}')