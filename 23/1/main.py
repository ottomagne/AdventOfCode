filename = 'input.txt'
nums = []
digits = list(map(str, tuple(range(10))))

def findDigit(line):
    for i in line:
        if i in digits:
            return i

with open(filename, 'r') as f:
    lines = f.read().split('\n')
lines = lines[:-1]
for l in lines:
    firstDigit = findDigit(l)
    secondDigit = findDigit(l[::-1])
    nums.append(int(firstDigit + secondDigit))

print(sum(nums))
