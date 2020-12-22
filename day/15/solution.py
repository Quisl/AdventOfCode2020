def parseFile():
    with open("input.txt", "r") as f:
        line = f.readline().replace("\n", "")
        numbers = line.split(",")
        numbers = list(map(int, numbers))
    return numbers


def part1():
    numbers = parseFile()
    lasttimes = {}

    for i in range(1, 2021):
        if i <= len(numbers):
            saynumber = numbers[i - 1]
        else:
            consider = lastround
            if consider in lasttimes:
                if len(lasttimes[consider]) == 1:
                    saynumber = 0
                else:
                    saynumber = (
                        lasttimes[consider][-1] - lasttimes[consider][-2]
                    )
            else:
                saynumber = 0
        if saynumber in lasttimes:
            lasttimes[saynumber].append(i)
        else:
            lasttimes[saynumber] = []
            lasttimes[saynumber].append(i)

        lastround = saynumber
    return saynumber


def part1():
    numbers = parseFile()
    lasttimes = {}

    for i in range(1, 30000001):
        if i <= len(numbers):
            saynumber = numbers[i - 1]
        else:
            consider = lastround
            if consider in lasttimes:
                if len(lasttimes[consider]) == 1:
                    saynumber = 0
                else:
                    saynumber = (
                        lasttimes[consider][-1] - lasttimes[consider][-2]
                    )
            else:
                saynumber = 0
        if saynumber in lasttimes:
            lasttimes[saynumber].append(i)
        else:
            lasttimes[saynumber] = []
            lasttimes[saynumber].append(i)

        lastround = saynumber
    return saynumber


print(part2())
