def parseFile():
    exercises = []
    with open("input.txt", "r") as f:
        for line in f:
            exercises.append(line.replace("\n", "").replace(" ", ""))
    return exercises


def findClosingBracket(exercise):
    counter = 1
    for pos, char in enumerate(exercise[1:]):
        if char == "(":
            counter += 1
        if char == ")":
            counter -= 1
        if counter == 0:
            return pos + 1
    return None


def findClosingBracket2(exercise):
    counter = 1
    for pos, char in enumerate(exercise[exercise.find("(") + 1 :]):
        if char == "(":
            counter += 1
        if char == ")":
            counter -= 1
        if counter == 0:
            return pos + 1 + exercise.find("(")
    return None


def getFirstElement(exercise):
    first = ""
    if exercise[0] != "(":
        first = exercise[0]
        return first, exercise[1:]
    else:
        openbpos = 0
        closebpos = findClosingBracket(exercise)
        first, subexercise = getFirstElement(
            exercise[openbpos + 1 : closebpos]
        )
        first = solve(subexercise, first)
        return first, exercise[closebpos + 1 :]


def solve(exercise, first):
    operator = exercise[0]
    exercise = exercise[1:]
    second, exercise = getFirstElement(exercise)
    result = eval(f"{first}{operator}{second}")
    if len(exercise) > 0:
        result = solve(exercise, result)
    return result


def part1():
    exercises = parseFile()
    solutions = []
    for exercise in exercises:
        first, exercise = getFirstElement(exercise)
        solutions.append(solve(exercise, first))
    return sum(solutions)


def getFirstElement2(exercise):
    first = ""
    if exercise[0] != "(":
        first = exercise[0]
        return first, exercise[1:]
    else:
        openbpos = 0
        closebpos = findClosingBracket(exercise)
        first, subexercise = getFirstElement(
            exercise[openbpos + 1 : closebpos]
        )
        first = solve(subexercise, first)
        return first, exercise[closebpos + 1 :]


def nextOperator(exercise):
    if "+" in exercise:
        position = exercise.find("+")
        operator = "+"
    elif "*" in exercise:
        position = exercise.find("*")
        operator = "*"
    else:
        position = 0
        operator = "F"
    return position, operator


def getPreviousNumber(exercise, position):
    counter = 0
    try:
        while exercise[position - 1 - counter] in "0123456789":
            if position - 1 - counter < 0:
                break
            counter += 1
    except IndexError:
        pass
    numberstart = position - counter
    numberend = position
    number = exercise[numberstart:numberend]
    return number, numberstart


def getFollowingNumber(exercise, position):
    counter = 0
    try:
        while exercise[position + 1 + counter] in "0123456789":
            counter += 1
    except IndexError:
        pass
    numberstart = position + 1
    numberend = position + 1 + counter
    number = exercise[numberstart:numberend]
    return number, numberend


def solve2(exercise):
    print("Loese: " + exercise)
    while "(" in exercise:
        pos = exercise.find("(")
        subexercise = exercise[pos + 1 : findClosingBracket2(exercise)]
        print("Subaufgabe:" + subexercise)
        subresult = solve2(subexercise)
        exercise = (
            exercise[:pos]
            + subresult
            + exercise[findClosingBracket2(exercise) + 1 :]
        )
        print("Klammer aufgeloest: " + exercise)
    # Rufe subaufgaben von sich selbst nochmal auf bis keine klammern mehr drin sind
    position, operator = nextOperator(exercise)
    first, firststart = getPreviousNumber(exercise, position)
    last, lastend = getFollowingNumber(exercise, position)
    if operator != "F":
        result = eval(f"{first}{operator}{last}")
        print("Ergebnis: " + str(result))
        exercise = exercise[:firststart] + str(result) + exercise[lastend:]
        result = solve2(exercise)
    else:
        result = exercise
    return result


def part2():
    exercises = parseFile()
    solutions = []
    exercise = "2*3+4*5+6"  # 154
    # first = getFirstElement2(exercise)
    # solutions.append(int(solve2(exercise)))
    for exercise in exercises:
        print("Solving: " + exercise)
        solutions.append(int(solve2(exercise)))
    return sum(solutions)


print(part2())

