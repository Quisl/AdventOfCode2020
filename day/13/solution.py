import numpy
import copy


def parseFile():
    with open("input.txt", "r") as f:
        timestamp = f.readline().replace("\n", "")
        busses = f.readline().replace("\n", "").split(",")
    return timestamp, busses


def prepareBusses(busses):
    while "x" in busses:
        busses.remove("x")
    busses = list(map(int, busses))
    return busses


def getNextBus(timestamp, busses):
    for i in range(timestamp + min(busses)):
        for bus in busses:
            if i % int(bus) == 0:
                if i >= timestamp:
                    return bus, i - timestamp
                    # print(f"Timestamp: {i} Bus: {bus}")
    return None


def findBusSequence(busses):
    timestamp = 1
    chainmax = len(busses)
    jumprange = 1
    while True:
        # print(timestamp)
        chain = 0
        counter = 0
        for counter, bus in enumerate(busses):
            if bus == 0:
                chain += 1
                continue
            if (timestamp + counter) % bus == 0:
                chain += 1
            else:
                if counter >= 1:
                    bussescopy = copy.deepcopy(busses)
                    while 0 in bussescopy:
                        bussescopy.remove(0)
                    # print(bussescopy[:counter])
                    if (
                        numpy.prod(bussescopy[: bussescopy.index(bus)])
                        > jumprange
                    ):
                        covered = numpy.array(
                            bussescopy[: bussescopy.index(bus)],
                            dtype=numpy.float64,
                        )
                        jumprange = numpy.prod(covered)
                        print(jumprange)
                break
        if chain == chainmax:
            return timestamp
        timestamp += jumprange


def part1():
    timestamp, busses = parseFile()
    busses = prepareBusses(busses)
    busid, minutes = getNextBus(int(timestamp), busses)
    return str(busid * minutes)


def xto0(x):
    if x == "x":
        return "0"
    return x


def part2():
    _, busses = parseFile()
    busses = list(map(xto0, busses))
    busses = list(map(int, busses))
    timestamp = findBusSequence(busses)
    return str(int(timestamp))


print(part2())
