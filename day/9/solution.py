import sys

sys.setrecursionlimit(9999)


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
                # print(f"{number} is valid: {i}+{j}")
                return True
    # print(f"{number} is not valid")
    return False


def findWeakness(invalid, numbers, start, end):
    for start in range(len(numbers)):
        for end in range(len(numbers)):
            if sum(numbers[start:end]) > invalid:
                break
            elif sum(numbers[start:end]) < invalid:
                continue
            elif sum(numbers[start:end]) == invalid:
                print(start)
                print(end)
                minimum = min(numbers[start:end])
                maximum = max(numbers[start:end])
                return minimum + maximum


#    if sum(numbers[start:end]) > invalid:
#        start = start + 1
#        end = start + 1
#    elif sum(numbers[start:end]) < invalid:
#        end = end + 1
#    elif sum(numbers[start:end]) == invalid:
#        result = start + end
#    if result == None:
#        result = findWeakness(invalid, numbers, start, end, result)
#    return result


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
