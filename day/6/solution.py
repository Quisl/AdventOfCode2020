def getGroupAnswersFromFile():
    groupAnswers = []
    answers = []
    with open("input.txt") as f:
        for line in f:
            if line == "\n":
                groupAnswers.append(answers)
                answers = []
            else:
                line = line.replace("\n", "")
                answers.append(line)
        groupAnswers.append(answers)

    return groupAnswers


def removeDoubleEntriesInGroupAnyone(group):
    groupAnswers = ""
    for member in group:
        groupAnswers = groupAnswers + member
    return "".join(set(groupAnswers))


def removeDoubleEntriesInGroupEveryone(group):
    groupAnswers = ""
    compare = group[0]
    for member in group[1:]:
        compare = set(compare) - (set(compare) - set(member))
    return "".join(compare)


def sumAnswers(groups):
    amount = 0
    for group in groups:
        amount += len(group)
    return amount


def part1():
    groups = getGroupAnswersFromFile()
    cleanGroups = []
    for group in groups:
        cleanGroups.append(removeDoubleEntriesInGroupAnyone(group))

    answerSum = sumAnswers(cleanGroups)
    return str(answerSum)


def part2():
    groups = getGroupAnswersFromFile()
    cleanGroups = []
    for group in groups:
        cleanGroups.append(removeDoubleEntriesInGroupEveryone(group))

    answerSum = sumAnswers(cleanGroups)
    return str(answerSum)


print(part2())
