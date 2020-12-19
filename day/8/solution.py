# class Instruction:
#    def __init__(self, name, value, linenumber):
#        self.name = name
#        self.value = value
#        self.linenumber = linenumber
#
#    def __str__(self):
#        return f"{self.linenumber}: {self.name}  {self.value}"
import copy


def parseFile():
    code = {}
    with open("input.txt", "r") as f:
        linenumber = 0
        for line in f:
            linenumber += 1
            linepart = line.split(" ")
            instructionname = linepart[0]
            value = linepart[1].replace("\n", "")
            code[linenumber] = (instructionname, value)
    return code


class Executor:
    def __init__(self):
        self.nextline = 1
        self.accumulator = 0
        self.visited = []

    def execute(self, code):
        while True:
            if self.nextline not in code:
                return self.accumulator, 0
            if self.nextline in self.visited:
                return self.accumulator, 1
            self.visited.append(self.nextline)
            if code[self.nextline][0] == "nop":
                self.nop(code[self.nextline][1])
            elif code[self.nextline][0] == "jmp":
                self.jmp(code[self.nextline][1])
            elif code[self.nextline][0] == "acc":
                self.acc(code[self.nextline][1])

    def nop(self, value):
        self.nextline += 1

    def jmp(self, value):
        self.nextline += int(value)

    def acc(self, value):
        self.accumulator += int(value)
        self.nextline += 1


def getPossibleCodes(code):
    codes = []
    for line in code:
        codecopy = copy.deepcopy(code)
        if code[line][0] == "nop":
            codecopy[line] = ("jmp", code[line][1])
            codes.append(codecopy)
        elif code[line][0] == "jmp":
            codecopy[line] = ("nop", code[line][1])
            codes.append(codecopy)
    return codes


def part2():
    codes = getPossibleCodes(parseFile())
    for code in codes:
        value = Executor().execute(code)
        print(value)
        if value[1] == 0:
            acc = value[0]
    return str(acc)


def part1():
    code = parseFile()
    acc = Executor().execute(code)[0]
    return str(acc)


print(part2())
