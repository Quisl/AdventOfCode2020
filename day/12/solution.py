import cmath
import math


class Command:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Ship:
    def __init__(self, x=0, y=0, direction=0):
        self.x = x
        self.y = y
        self.direction = direction

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __N(self, value):
        self.y += value

    def __S(self, value):
        self.y -= value

    def __E(self, value):
        self.x += value

    def __W(self, value):
        self.x -= value

    def __L(self, value):
        self.direction += value
        while self.direction >= 360:
            self.direction -= 360

    def __R(self, value):
        self.direction -= value
        while self.direction < 0:
            self.direction += 360

    def __F(self, value):
        rho = value
        phi = math.radians(self.direction)
        cart = cmath.rect(rho, phi)
        self.x += round(cart.real, 2)
        self.y += round(cart.imag, 2)

    def executeCommand(self, command: Command):
        if command.name == "N":
            self.__N(command.value)
        if command.name == "S":
            self.__S(command.value)
        if command.name == "E":
            self.__E(command.value)
        if command.name == "W":
            self.__W(command.value)
        if command.name == "L":
            self.__L(command.value)
        if command.name == "R":
            self.__R(command.value)
        if command.name == "F":
            self.__F(command.value)


class Ship2:
    def __init__(self, x=0, y=0, wx=10, wy=1):
        self.x = x
        self.y = y
        self.wx = wx
        self.wy = wy

    def __str__(self):
        return f"ship: ({self.x}, {self.y}) (wp: ({self.wx},{self.wy}))"

    def __N(self, value):
        self.wy += value

    def __S(self, value):
        self.wy -= value

    def __E(self, value):
        self.wx += value

    def __W(self, value):
        self.wx -= value

    def __L(self, value):
        rho, phi = cmath.polar(complex(self.wx, self.wy))
        phi = math.degrees(phi)
        phi += value
        phi = math.radians(phi)
        cart = cmath.rect(rho, phi)
        self.wx = cart.real
        self.wy = cart.imag

    def __R(self, value):
        rho, phi = cmath.polar(complex(self.wx, self.wy))
        phi = math.degrees(phi)
        phi -= value
        phi = math.radians(phi)
        cart = cmath.rect(rho, phi)
        self.wx = cart.real
        self.wy = cart.imag

    def __F(self, value):
        for _ in range(value):
            self.x += self.wx
            self.y += self.wy

    def executeCommand(self, command: Command):
        if command.name == "N":
            self.__N(command.value)
        if command.name == "S":
            self.__S(command.value)
        if command.name == "E":
            self.__E(command.value)
        if command.name == "W":
            self.__W(command.value)
        if command.name == "L":
            self.__L(command.value)
        if command.name == "R":
            self.__R(command.value)
        if command.name == "F":
            self.__F(command.value)


def parseFile():
    commands = []
    with open("input.txt", "r") as f:
        for line in f:
            commandname = line[0]
            value = line[1:].replace("\n", "")
            commands.append(Command(commandname, int(value)))
    return commands


def part1():
    commands = parseFile()
    ship = Ship()
    for command in commands:
        ship.executeCommand(command)
        print(ship)
    distance = abs(ship.x) + abs(ship.y)
    return str(distance)


def part2():
    commands = parseFile()
    ship = Ship2()
    for command in commands:
        ship.executeCommand(command)
        print(ship)
    distance = int(abs(ship.x) + abs(ship.y))
    return str(distance)


print(part2())
