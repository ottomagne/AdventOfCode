from math import inf
filename = 'input.txt'
nums = []
digits = list(map(str, tuple(range(10)))) + ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
wordToDigits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def findFirstDigit(line):
    digitsInLine = list(filter(lambda x: line.find(x) != -1, digits))
    minIndex = inf
    firstDigit = 0
    for digit in digitsInLine:
        index = line.find(digit)
        if index < minIndex:
            minIndex = index
            firstDigit = digit
    try:
        return int(firstDigit)
    except ValueError:
        return wordToDigits[firstDigit]

def findSecondDigit(line):
    digitsInLine = list(filter(lambda x: line.rfind(x) != -1, digits))
    maxIndex = -1
    secondDigit = inf
    for digit in digitsInLine:
        index = line.rfind(digit)
        if index > maxIndex:
            maxIndex = index
            secondDigit = digit
    try:
        return int(secondDigit)
    except ValueError:
        return wordToDigits[secondDigit]

with open(filename, 'r') as f:
    lines = f.read().split('\n')
lines = lines[:-1]
for l in lines:
    firstDigit, secondDigit = findFirstDigit(l), findSecondDigit(l)
    nums.append(int(str(firstDigit) + str(secondDigit)))

print(sum(nums))
