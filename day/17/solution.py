from copy import deepcopy


class Universe:
    def __init__(self):
        self.universe = {}

    def countActive(self):
        counter = 0
        for key in self.universe:
            if self.universe[key] == True:
                counter += 1
        return counter

    def getCube(self, coord):
        if coord in self.universe:
            return self.universe[coord]
        return False

    def cycleTrue(self, coords):
        neighbours = self.getAllNeighbours(coords)
        activeNeighbours = 0
        for neighbour in neighbours:
            if self.getCube(neighbour):
                activeNeighbours += 1
        if activeNeighbours == 2 or activeNeighbours == 3:
            return True
        return False

    def cycleFalse(self, coords):
        neighbours = self.getAllNeighbours(coords)
        activeNeighbours = 0
        for neighbour in neighbours:
            if self.getCube(neighbour):
                activeNeighbours += 1
        if activeNeighbours == 3:
            return True
        return False

    def cycle(self):
        newuni = deepcopy(self.universe)
        minx, maxx = self.getMinMax(0, self.possibleCubes)
        miny, maxy = self.getMinMax(1, self.possibleCubes)
        minz, maxz = self.getMinMax(2, self.possibleCubes)
        for z in range(minz, maxz + 1):
            for y in range(miny, maxy + 1):
                for x in range(minx, maxx + 1):
                    value = self.getCube((x, y, z))
                    if value:
                        newuni[(x, y, z)] = self.cycleTrue((x, y, z))
                    elif not value:
                        newuni[(x, y, z)] = self.cycleFalse((x, y, z))
        self.universe = newuni

    def getMinMax(self, axis, cubes):
        minimum = 0
        maximum = 0
        for cube in cubes:
            if cube[axis] < minimum:
                minimum = cube[axis]
            if cube[axis] > maximum:
                maximum = cube[axis]
        return minimum, maximum

    def __str__(self):
        minx, maxx = self.getMinMax(0, self.relevantCubes)
        miny, maxy = self.getMinMax(1, self.relevantCubes)
        minz, maxz = self.getMinMax(2, self.relevantCubes)
        output = ""
        for z in range(minz, maxz + 1):
            output += f"\nz={z}\n"
            for y in range(miny, maxy + 1):
                output += "\n"
                for x in range(minx, maxx + 1):
                    value = self.getCube((x, y, z))
                    if value == True:
                        output += "#"
                    elif value == False:
                        output += "."
        return output

    def parseFile(self):
        with open("input.txt", "r") as f:
            for y, line in enumerate(f):
                line = line.replace("\n", "")
                for x, char in enumerate(line):
                    if char == ".":
                        self.universe[(x, y, 0)] = False
                    elif char == "#":
                        self.universe[(x, y, 0)] = True

    @staticmethod
    def getAllNeighbours(coord):
        neighbours = []
        for xm in range(-1, 2):
            for ym in range(-1, 2):
                for zm in range(-1, 2):
                    neighbours.append(
                        (coord[0] + xm, coord[1] + ym, coord[2] + zm)
                    )
        neighbours.pop(neighbours.index(coord))
        return neighbours

    @property
    def possibleCubes(self):
        rc = []
        for key in self.universe:
            rc.append(key)
            for neighbour in self.getAllNeighbours(key):
                rc.append(neighbour)
        return rc

    @property
    def relevantCubes(self):
        rc = []
        for key in self.universe:
            rc.append(key)
        return rc


class Universe4d(Universe):
    def __init__(self):
        self.universe = {}

    def cycle(self):
        newuni = deepcopy(self.universe)
        minx, maxx = self.getMinMax(0, self.possibleCubes)
        miny, maxy = self.getMinMax(1, self.possibleCubes)
        minz, maxz = self.getMinMax(2, self.possibleCubes)
        minw, maxw = self.getMinMax(3, self.possibleCubes)
        for w in range(minw, maxw + 1):
            for z in range(minz, maxz + 1):
                for y in range(miny, maxy + 1):
                    for x in range(minx, maxx + 1):
                        value = self.getCube((x, y, z, w))
                        if value:
                            newuni[(x, y, z, w)] = self.cycleTrue((x, y, z, w))
                        elif not value:
                            newuni[(x, y, z, w)] = self.cycleFalse(
                                (x, y, z, w)
                            )
        self.universe = newuni

    def parseFile(self):
        with open("input.txt", "r") as f:
            for y, line in enumerate(f):
                line = line.replace("\n", "")
                for x, char in enumerate(line):
                    if char == ".":
                        self.universe[(x, y, 0, 0)] = False
                    elif char == "#":
                        self.universe[(x, y, 0, 0)] = True

    @staticmethod
    def getAllNeighbours(coord):
        neighbours = []
        for xm in range(-1, 2):
            for ym in range(-1, 2):
                for zm in range(-1, 2):
                    for wm in range(-1, 2):
                        neighbours.append(
                            (
                                coord[0] + xm,
                                coord[1] + ym,
                                coord[2] + zm,
                                coord[3] + wm,
                            )
                        )
        neighbours.pop(neighbours.index(coord))
        return neighbours


def part1():
    uni = Universe()
    uni.parseFile()
    for i in range(6):
        uni.cycle()
    return str(uni.countActive())


def part2():
    uni = Universe4d()
    uni.parseFile()
    for i in range(6):
        uni.cycle()
    return str(uni.countActive())


print(part2())
