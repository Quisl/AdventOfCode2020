def readFile():
    numberlist = []
    with open("input.txt", "r") as f:
        for line in f:
            numberlist.append(int(line.replace("\n", "")))
    return numberlist


def getPrevious(c, numbers):
    if c < 25:
        return None
    return numbers[c - 25 : c]


def isValid(number, previous):
    for i in previous:
        for j in previous[previous.index(i) :]:
            if i + j == number:
                return True
    return False


def findWeakness(invalid, numbers, start, end):
    for start in range(len(numbers)):
        for end in range(len(numbers)):
            if sum(numbers[start:end]) > invalid:
                break
            elif sum(numbers[start:end]) < invalid:
                continue
            elif sum(numbers[start:end]) == invalid:
                minimum = min(numbers[start:end])
                maximum = max(numbers[start:end])
                return minimum + maximum


def part2():
    numbers = readFile()
    invalid = int(part1())
    # invalid = 53
    weakness = findWeakness(invalid=invalid, numbers=numbers, start=0, end=1)
    return weakness


def part1():
    numbers = readFile()
    for c, number in enumerate(numbers):
        prev = getPrevious(c, numbers)
        if prev is not None:
            if not isValid(number, prev):
                return str(number)
    return ""


print(part2())
