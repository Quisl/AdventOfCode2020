def part1():
    x = 3
    treecounter = 0
    with open("input.txt", "r") as f:
        next(f)
        for line in f:
            line = line.replace("\n", "")
            x += 3
            x = x % len(line)
            if line[x] == "#":
                treecounter += 1
            # line[x % len(line)] = "X"
            # print(repr(line))

    return str(treecounter)


print(part1())
