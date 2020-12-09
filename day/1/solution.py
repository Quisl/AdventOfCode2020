numbers = open("input.txt", "r").read().split("\n")


def part1():
    for i in numbers:
        for j in numbers[numbers.index(i) :]:
            if int(i) + int(j) == 2020:
                return int(i) * int(j)


def part2():
    for i in numbers:
        for j in numbers[numbers.index(i) :]:
            for x in numbers[numbers.index(j) :]:
                if int(i) + int(j) + int(x) == 2020:
                    return int(i) * int(j) * int(x)


print(str(part1()))
print(str(part2()))
