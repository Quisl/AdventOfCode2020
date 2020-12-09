import re


def part1():
    pattern = r"(\d*)-(\d*) (\w): (.*)"
    counter = 0
    with open("input.txt", "r") as f:
        for line in f:
            x = re.match(pattern, line)
            minimum, maximum, character, pw = x.group(1, 2, 3, 4)
            amount = pw.count(character)
            if amount >= int(minimum) and amount <= int(maximum):
                counter += 1
    return str(counter)


def part2():
    pattern = r"(\d*)-(\d*) (\w): (.*)"
    counter = 0
    with open("input.txt", "r") as f:
        for line in f:
            x = re.match(pattern, line)
            pos1, pos2, character, pw = x.group(1, 2, 3, 4)
            aValid = bValid = False

            if pw[int(pos1) - 1] == character:
                aValid = True
            if pw[int(pos2) - 1] == character:
                bValid = True
            if aValid ^ bValid:
                counter += 1

    return str(counter)


# print(part1())
print(part2())
