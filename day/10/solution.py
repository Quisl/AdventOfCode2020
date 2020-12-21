def parseFile():
    adapters = []
    with open("input.txt", "r") as f:
        for line in f:
            adapters.append(int(line.replace("\n", "")))
    return adapters


def findNext(adapter, adapters):
    adapter = int(adapter)
    if adapter + 1 in adapters:
        return 1
    if adapter + 2 in adapters:
        return 2
    if adapter + 3 in adapters:
        return 3


def findWays(adapters):
    memory = [1]
    for adapterpos in range(1, len(adapters)):
        amount = 0
        for x in range(adapterpos, 0, -1):
            if adapters[adapterpos] - adapters[x - 1] <= 3:
                amount += memory[x - 1]
            else:
                break
        memory.append(amount)
    return memory[-1]


def part2():
    adapters = parseFile()
    adapters.append(max(adapters) + 3)
    adapters.append(0)
    adapters.sort()
    total = findWays(adapters)
    return total


def part1():
    adapters = parseFile()
    mydevice = max(adapters) + 3
    adapters.append(mydevice)
    adapters.append(0)
    differences = {1: 0, 2: 0, 3: 0}
    adapters.sort()
    for current in adapters[:-1]:
        difference = findNext(current, adapters)
        differences[difference] += 1
    return str(differences[1] * differences[3])


print(part2())
