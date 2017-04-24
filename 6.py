'''
trials = 909

nothing = "90052.txt"

for i in range(trials):
    print(i)
    file = open("".join(["./channel/", nothing]), "r").read()
    print(file)
    words = file.split()
    nothing = "".join([words[-1], ".txt"])
'''
import requests
import zipfile
import io

r = requests.get('http://www.pythonchallenge.com/pc/def/channel.html')
print(r.text)
r = requests.get('http://www.pythonchallenge.com/pc/def/channel.zip')
zip = zipfile.ZipFile(io.BytesIO(r.content))
nothing = "90052.txt"
try:
    while type(int(nothing.split(".")[0])) == int:
        text = str(zip.open(nothing).read())
        textlist = text.strip("'").split()
        nothing = "".join([textlist[-1], ".txt"])
        # print(nothing)
except ValueError:
    pass

print(text)

nothing = "90052.txt"
comments = []
try:
    while type(int(nothing.split(".")[0])) == int:
        info = zip.getinfo(nothing)
        comments.append(info.comment.decode("utf-8"))
        text = str(zip.open(nothing).read())
        textlist = text.strip("'").split()
        nothing = "".join([textlist[-1], ".txt"])
        # print(nothing)
except ValueError:
    pass

print("Output below")
line = []
for element in comments:
    if element == '\n':
        print(''.join(line))
        line = []
    else:
        line.append(element)
