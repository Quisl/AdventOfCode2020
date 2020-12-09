import numpy


def part1():
    x = 0
    treecounter = 0
    with open("input.txt", "r") as f:
        next(f)
        for line in f:
            line = line.replace("\n", "")
            x += 3
            x = x % len(line)
            if line[x] == "#":
                treecounter += 1
            line = list(line)
            line[x % len(line)] = "X"
            line = "".join(line)
            print(repr(line))

    return str(treecounter)


def part2():
    toCheck = [
        {"x": 1, "y": 1},
        {"x": 3, "y": 1},
        {"x": 5, "y": 1},
        {"x": 7, "y": 1},
        {"x": 1, "y": 2},
    ]
    results = []
    for check in toCheck:
        treecounter = 0
        x = 0
        with open("input.txt", "r") as f:
            next(f)
            for line in f:
                for i in range(int(check["y"]) - 1):
                    line = next(f)
                line = line.replace("\n", "")
                x += check["x"]
                x = x % len(line)
                if line[x] == "#":
                    treecounter += 1

        results.append(treecounter)
    erg = 1
    print(results)
    for result in results:
        erg = erg * result
    return str(erg)


print(part2())
