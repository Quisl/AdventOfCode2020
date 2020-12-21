import copy


def parseFile():
    grid = []
    with open("input.txt", "r") as f:
        for line in f:
            line = line.replace("\n", "")
            x = list(line)
            grid.append(x)
    return grid


def changeSeatL(grid, ypos, xpos):
    neighbours = []
    for ymod in range(-1, 2):
        for xmod in range(-1, 2):
            if ymod == 0 and xmod == 0:
                continue
            try:
                if ypos + ymod >= 0 and xpos + xmod >= 0:
                    neighbours.append(grid[ypos + ymod][xpos + xmod])
            except IndexError:
                pass
    if not "#" in neighbours:
        return "#"
    return "L"


def changeSeatHash(grid, ypos, xpos):
    amount = 0
    for ymod in range(-1, 2):
        for xmod in range(-1, 2):
            if ymod == 0 and xmod == 0:
                continue
            try:
                if not ypos + ymod < 0 and not xpos + xmod < 0:
                    if grid[ypos + ymod][xpos + xmod] == "#":
                        amount += 1
            except IndexError:
                pass
    if amount >= 4:
        return "L"
    return "#"


def changeSeatL2(grid, ypos, xpos):
    neighbours = []
    for ymod in range(-1, 2):
        for xmod in range(-1, 2):
            if ymod == 0 and xmod == 0:
                continue
            for modmult in range(1, max([len(grid), len(grid[0])])):
                try:
                    if (
                        ypos + ymod * modmult >= 0
                        and xpos + xmod * modmult >= 0
                    ):
                        neighbours.append(
                            grid[ypos + ymod * modmult][xpos + xmod * modmult]
                        )
                    if (
                        grid[ypos + ymod * modmult][xpos + xmod * modmult]
                        != "."
                    ):
                        break
                except IndexError:
                    pass
    if not "#" in neighbours:
        return "#"
    return "L"


def changeSeatHash2(grid, ypos, xpos):
    amount = 0
    for ymod in range(-1, 2):
        for xmod in range(-1, 2):
            if ymod == 0 and xmod == 0:
                continue
            for modmult in range(1, max([len(grid), len(grid[0])])):
                try:
                    if (
                        not ypos + ymod * modmult < 0
                        and not xpos + xmod * modmult < 0
                    ):
                        if (
                            grid[ypos + ymod * modmult][xpos + xmod * modmult]
                            == "#"
                        ):
                            amount += 1
                            break
                    if (
                        grid[ypos + ymod * modmult][xpos + xmod * modmult]
                        != "."
                    ):
                        break
                except IndexError:
                    pass
    if amount >= 5:
        return "L"
    return "#"


def countOccupied(grid):
    amount = 0
    for line in grid:
        for character in line:
            if character == "#":
                amount += 1
    return amount


def playRound(grid):
    newgrid = copy.deepcopy(grid)
    for ypos, line in enumerate(grid):
        for xpos, character in enumerate(line):
            if character == "L":
                newgrid[ypos][xpos] = changeSeatL(grid, ypos, xpos)
            elif character == "#":
                newgrid[ypos][xpos] = changeSeatHash(grid, ypos, xpos)
            elif character == ".":
                pass
    return newgrid


def playRound2(grid):
    newgrid = copy.deepcopy(grid)
    for ypos, line in enumerate(grid):
        for xpos, character in enumerate(line):
            if character == "L":
                newgrid[ypos][xpos] = changeSeatL2(grid, ypos, xpos)
            elif character == "#":
                newgrid[ypos][xpos] = changeSeatHash2(grid, ypos, xpos)
            elif character == ".":
                pass
    return newgrid


def show(grid):
    print("----------")
    for line in grid:
        print("".join(line))
    print("----------")


def part1():
    grid = parseFile()
    while True:
        # show(grid)
        newgrid = playRound(copy.deepcopy(grid))
        if grid == newgrid:
            break
        else:
            grid = newgrid
    amount = countOccupied(grid)
    show(grid)
    return amount


def part2():
    grid = parseFile()
    while True:
        # show(grid)
        newgrid = playRound2(copy.deepcopy(grid))
        if grid == newgrid:
            break
        else:
            grid = newgrid
    amount = countOccupied(grid)
    show(grid)
    return amount


print(part2())
