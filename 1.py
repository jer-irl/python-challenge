import string
alphabet = string.ascii_lowercase


def buildDict(shift):
    inp = list(alphabet)
    out = list(alphabet)
    for i in range(shift):
        out.append(out.pop(0))
    dict = {}
    for i in range(len(inp)):
        dict[inp[i]] = out[i]
    return dict


def convertText(text, dict):
    textList = list(text)
    outList = []
    for letter in textList:
        if letter in list(alphabet):
            outList.append(dict[letter])
        else:
            outList.append(letter)
    return ''.join(outList)

translation = convertText("g fmnc wms bgblr rpylqjyrc \
            gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb \
            gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle \
            qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.",
                          buildDict(2))
print(translation)

answer = convertText("http://www.pythonchallenge.com/pc/def/map.html",
                     buildDict(2))
print(answer)
