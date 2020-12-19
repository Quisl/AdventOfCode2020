def decoder(rowstring, minid=0, maxid=127):
    if rowstring[0] == "F" or rowstring[0] == "L":
        maxid = minid + ((maxid - 1 - minid) / 2)
    elif rowstring[0] == "B" or rowstring[0] == "R":
        minid = (minid + maxid + 1) / 2
    if len(rowstring) > 1:
        result = decoder(rowstring=rowstring[1:], minid=minid, maxid=maxid)
    else:
        result = None
        return int(minid)
    return result


def parseLine(inputstring):
    row = decoder(rowstring=inputstring[:7], minid=0, maxid=127)
    seat = decoder(rowstring=inputstring[7:], minid=0, maxid=7)
    return row, seat


def part1():
    seatIDs = []
    with open("input.txt", "r") as f:
        for line in f:
            seatID = 0
            row, seat = parseLine(line)
            seatID = row * 8 + seat
            seatIDs.append(seatID)
    return str(max(seatIDs))


def part2():
    seatIDs = []
    with open("input.txt", "r") as f:
        for line in f:
            seatID = 0
            row, seat = parseLine(line)
            seatID = row * 8 + seat
            seatIDs.append(seatID)
    seatIDs.sort()
    for i in range(6, 894):
        if i not in seatIDs:
            value = i

    return str(value)


# print(part1())
print(part2())

