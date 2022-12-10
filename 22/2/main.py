filename = 'input.txt'
instructions = None
totalScore = 0

def resolve(a, b):
    sum = 0
    if a == "A":
        if b == "X":
            sum += 3
        elif b == "Y":
            sum += 1
        elif b == "Z":
            sum += 2
    elif a == "B":
        if b == "X":
            sum += 1
        elif b == "Y":
            sum += 2
        elif b == "Z":
            sum += 3
    elif a == "C":
        if b == "X":
            sum += 2
        elif b == "Y":
            sum += 3
        elif b == "Z":
            sum += 1
    return sum + (ord(b) - 88)*3

with open(filename, 'r') as f:
    instructions = f.readlines()

for i in instructions:
    a, b = i.split()
    totalScore += resolve(a, b)

print(totalScore)