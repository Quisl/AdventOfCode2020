import copy


class Bag:
    def __init__(self, name: str, storage: list):
        self.name = name
        self.storage = storage

    def __str__(self):
        return f"{self.name} can store: {self.storage}"


def getNameFromLine(line):
    wordlist = line.split(" ")
    return " ".join(wordlist[:2])


def getStorageFromLine(line):
    wordlist = line.split(" ")[4:]
    returnlist = []
    if wordlist[0] != "no":
        for wordlist in (" ".join(wordlist)).split(", "):
            for i in range(int(wordlist[0])):
                wordstring = copy.deepcopy(wordlist.split(" "))

                name = " ".join(wordstring[1:3])
                returnlist.append(name)
    return returnlist


def parseLine(line):
    "returns the bag defined in this line"
    name = getNameFromLine(line)
    storage = getStorageFromLine(line)
    bag = Bag(name, storage)
    return bag


def findUpperBags(name, bags):
    newbags = []
    for bag in bags:
        if name in bag.storage:
            newbags.append(bag)
            upperBags = findUpperBags(bag.name, bags)
            if upperBags != None:
                for ubag in upperBags:
                    newbags.append(ubag)

    if newbags != []:
        return newbags


def readFile():
    bags = []
    with open("input.txt", "r") as f:
        for line in f:
            bags.append(parseLine(line.replace("\n", "")))
    return bags


def part1():
    bags = readFile()
    goldbags = findUpperBags("shiny gold", bags)
    for bag in goldbags:
        print(bag)
    amount = len(set(goldbags))
    return str(amount)


def countBagsInBag(bags, bagname, amount=0):
    for bag in bags:
        if bag.name == bagname:
            amount += 1
            if len(bag.storage) != 0:
                # amount += len(bag.storage)
                for ubagname in bag.storage:
                    amount = countBagsInBag(
                        bags=bags, bagname=ubagname, amount=amount
                    )
    return amount


def part2():
    bags = readFile()
    amount = countBagsInBag(bags, bagname="shiny gold") - 1
    return str(amount)


print(part2())

