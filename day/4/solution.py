def part1():
    passports = []
    passport = {}
    with open("input.txt", "r") as f:
        for line in f:
            if line == "\n":
                passports.append(passport)
                passport = {}
                line = next(f)
            entryinline = line.replace("\n", "").split(" ")
            for entry in entryinline:
                key = entry.split(":")[0]
                value = entry.split(":")[1]
                passport[key] = value

    passports.append(passport)
    amount = 0
    for passport in passports:
        if {
            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid",
        } <= passport.keys():
            amount += 1
    return str(amount)


def part2():
    passports = []
    passport = {}
    with open("input.txt", "r") as f:
        for line in f:
            if line == "\n":
                passports.append(passport)
                passport = {}
                line = next(f)
            entryinline = line.replace("\n", "").split(" ")
            for entry in entryinline:
                key = entry.split(":")[0]
                value = entry.split(":")[1]
                passport[key] = value

    passports.append(passport)
    amount = 0
    for passport in passports:
        if {
            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid",
        } <= passport.keys():
            if (
                2002 >= int(passport["byr"]) >= 1920
                and 2010 <= int(passport["iyr"]) <= 2020
                and 2020 <= int(passport["eyr"]) <= 2030
                and checkHeight(passport["hgt"])
                and checkHCL(passport["hcl"])
                and checkECL(passport["ecl"])
                and checkPID(passport["pid"])
            ):
                amount += 1
    return str(amount)


def checkPID(pid):
    try:
        int(pid)
    except ValueError:
        return False
    if len(pid) == 9:
        return True
    return False


def checkECL(ecl):
    if ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    return False


def checkHeight(height):
    if height[-2:] == "cm":
        if 150 <= int(height[:-2]) <= 193:
            return True
    elif height[-2:] == "in":
        if 59 <= int(height[:-2]) <= 76:
            return True
    return False


def checkHCL(colour):
    if not colour[0] == "#":
        return False
    try:
        int(colour[1:], 16)
    except ValueError:
        return False
    if len(colour[1:]) != 6:
        return False
    return True


print(part2())
