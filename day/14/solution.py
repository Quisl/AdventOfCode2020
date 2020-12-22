import re
from copy import deepcopy


class Command:
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value


def parseFile():
    commands = []
    with open("input.txt", "r") as f:
        for line in f:
            line = line.replace("\n", "")
            pattern = "([][\w.]*) = (.*)"
            findings = re.search(pattern, line)
            variable = findings.group(1)
            value = findings.group(2)
            commands.append(Command(variable, value))

    return commands


def calcValue(mask, value):
    binvalue = bin(int(value))[2:]
    while len(binvalue) != len(mask):
        binvalue = "0" + binvalue
    for i in range(len(mask) - 1, -1, -1):
        if mask[i] == "X":
            pass
        if mask[i] == "0":
            binvaluelist = list(binvalue)
            binvaluelist[i] = "0"
            binvalue = "".join(binvaluelist)
        if mask[i] == "1":
            binvaluelist = list(binvalue)
            binvaluelist[i] = "1"
            binvalue = "".join(binvaluelist)
    return int(binvalue, 2)


def execute(commands):
    mem = {}
    mask = ""
    for command in commands:
        if command.variable == "mask":
            mask = command.value
        else:
            mem[command.variable[4:-1]] = calcValue(mask, command.value)
    return mem


def substitute(binadress):
    stringlist = list(binadress)
    binadresses = []
    for pos in range(len(stringlist)):
        if stringlist[pos] == "X":
            stringlist[pos] = "0"
            binadresses.append("".join(stringlist))
            stringlist[pos] = "1"
            binadresses.append("".join(stringlist))
            return binadresses


def calcAdress(mask, adress):
    binadress = bin(int(adress))[2:]
    binadresses = []
    adresses = []
    while len(binadress) != len(mask):
        binadress = "0" + binadress
    for i in range(len(mask) - 1, -1, -1):
        if mask[i] == "X":
            binadresslist = list(binadress)
            binadresslist[i] = "X"
            binadress = "".join(binadresslist)
        if mask[i] == "0":
            pass
        if mask[i] == "1":
            binadresslist = list(binadress)
            binadresslist[i] = "1"
            binadress = "".join(binadresslist)
    binadresses.append(binadress)

    for binadress in binadresses:
        if "X" in binadress:
            for subbinadress in substitute(binadress):
                binadresses.append(subbinadress)
        else:
            adresses.append(int(binadress, 2))

    return adresses


def execute2(commands):
    mem = {}
    mask = ""
    for command in commands:
        if command.variable == "mask":
            mask = command.value
        else:
            adresses = calcAdress(mask, command.variable[4:-1])
            for adress in adresses:
                mem[adress] = int(command.value)
    return mem


def part1():
    commands = parseFile()
    mem = execute(commands)
    summe = 0
    for key in mem:
        summe += mem[key]
    return str(summe)


def part2():
    commands = parseFile()
    mem = execute2(commands)
    summe = 0
    for key in mem:
        summe += mem[key]
    return str(summe)


print(part2())

