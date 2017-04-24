import requests

'''
times = 100
nothings = [12345]
for i in range(times):
    part1 = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    part2 = str(nothings[-1])
    address = "".join([part1, part2])
    site = requests.get(address)
    source = site.text
    words = source.split()
    nothings.append(words[-1])
    print("Completed iteration", i + 1)

site = requests.get("".join(['http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=', '16044']))
source = site.text
print(nothings)
print(source)
'''

times2 = 400
nothings2 = [str(16044 / 2)]
for i in range(times2):
    part1 = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    part2 = nothings2[-1]
    address = "".join([part1, part2])
    site = requests.get(address)
    source = site.text
    words = source.split()
    nothings2.append(words[-1])
    print("Completed iteration", i + 1)

print(nothings2)
