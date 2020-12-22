def parseFile():
    fields = {}
    nearbytickets = []
    yourticket = ""
    with open("input.txt", "r") as f:
        for _ in range(20):
            line = f.readline().replace("\n", "")
            line = line.split(":")
            key = line[0]
            valuestring = line[1].replace(" ", "").split("or")
            ranges = []
            for rang in valuestring:
                ranges.append(
                    range(
                        int(rang.split("-")[0]), int(rang.split("-")[1]) + 1,
                    )
                )

            fields[key] = ranges
        f.readline()
        f.readline()
        yourticket = f.readline().replace("\n", "").split(",")
        f.readline()
        f.readline()
        for line in f:
            nearbytickets.append(line.replace("\n", "").split(","))
    return fields, yourticket, nearbytickets


def checkIfInRange(value, fields):
    for key in fields:
        for r in fields[key]:
            if int(value) in r:
                return True
    return False


def getInvalidValuesFromTicket(ticket, fields):
    invalidcounter = 0
    for value in ticket:
        if not checkIfInRange(value, fields):
            invalidcounter += int(value)
    return invalidcounter


def part1():
    fields, _, nearbytickets = parseFile()
    totalinvalids = 0
    for ticket in nearbytickets:
        invalids = getInvalidValuesFromTicket(ticket, fields)
        totalinvalids += invalids
    return totalinvalids


def checkValuesInRanges(values, ranges):
    possible = True
    for value in values:
        if not int(value) in ranges[0] and not int(value) in ranges[1]:
            possible = False
    return possible


def guessRow(tickets, fields):
    columnvalues = {}
    results = {}
    for ticket in tickets:
        for i, value in enumerate(ticket):
            if i in columnvalues:
                columnvalues[i].append(value)
            else:
                columnvalues[i] = []
                columnvalues[i].append(value)
    for key in fields:
        for column in columnvalues:
            possible = checkValuesInRanges(columnvalues[column], fields[key])
            if possible:
                if key in results:
                    results[key].append(column)
                else:
                    results[key] = []
                    results[key].append(column)

    return results


def part2():
    fields, yourticket, nearbytickets = parseFile()
    validtickets = []
    validtickets.append(yourticket)
    for ticket in nearbytickets:
        if getInvalidValuesFromTicket(ticket, fields) == 0:
            validtickets.append(ticket)

    results = guessRow(validtickets, fields)
    finalresults = {}
    found = []
    while len(found) < 20:
        for key in results:
            if len(results[key]) == 1:
                found.append(results[key][0])
                finalresults[key] = results[key][0]
        for key in results:
            try:
                results[key].pop(results[key].index(found[-1]))
            except ValueError:
                pass
    toMultiply = []
    print(finalresults)
    for key in finalresults:
        if "departure" in key:
            toMultiply.append(int(yourticket[finalresults[key]]))
    output = 1
    print(toMultiply)
    for m in toMultiply:
        output = output * m
    return str(output)


print(part2())
