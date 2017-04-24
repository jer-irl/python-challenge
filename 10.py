# a = [1, 11, 21, 1211, 111221,
# len(a[30]) = ?


def doStep(representation):
    for i in range(len(representation) - 1):
        if representation[i][0] == representation[i + 1][0]:
            num = representation[i][1] + representation[i + 1][1]
            val = representation[i][0]
            del representation[i + 1]
            del representation[i]
            representation.insert(i, (val, num))
            return representation


def isComplete(representation):
    response = True
    for i in range(len(representation) - 1):
        if representation[i][0] == representation[i + 1][0]:
            response = False
    return response


def getNextNum(inputint):
    listed = map(int, str(inputint))
    representation = [(x, 1) for x in listed]
    while not isComplete(representation):
        representation = doStep(representation)
    outlist = []
    for elem in representation:
        outlist.append(elem[1])
        outlist.append(elem[0])
    return int(''.join(map(str, outlist)))


a = [1]
for i in range(30):
    a.append(getNextNum(a[i]))

print("Final value: ", len(str(a[30])))
