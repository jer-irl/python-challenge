import requests
import pickle

r = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
file = open('5file', 'wb')
file.write(r.content)
file = open('5file', 'rb')
translate = pickle.load(file)
output = []
i = -1
for line in translate:
    i += 1
    output.append("")
    for tuple in line:
        for iter in range(tuple[1]):
            output[i] = output[i] + tuple[0]
outstring = ""
for line in output:
    outstring = outstring + line + '\n'
print(outstring)

print(requests.get('http://www.pythonchallenge.com/pc/def/peak.html').text)
