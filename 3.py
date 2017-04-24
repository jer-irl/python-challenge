import requests
import string
import time

site = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
source = site.text
mess = source.split('<!--')[-1].replace('-->', '')
mess = mess.strip()
letters = list(mess)
begin = time.clock()
results = []
for i in range(len(letters)):
    if letters[i] in list(string.ascii_uppercase):
        continue
    elif letters[i] in list(string.ascii_lowercase):
        try:
            if letters[i - 3] in list(string.ascii_uppercase) and \
                 letters[i - 4] in list(string.ascii_lowercase) and \
                 letters[i + 4] in list(string.ascii_lowercase) and \
                 letters[i - 2] in list(string.ascii_uppercase) and \
                 letters[i - 1] in list(string.ascii_uppercase) and \
                 letters[i + 1] in list(string.ascii_uppercase) and \
                 letters[i + 2] in list(string.ascii_uppercase) and \
                 letters[i + 3] in list(string.ascii_uppercase):
                results.append(letters[i])
        except:
            pass
end = time.clock()
print(results)
print("".join(results))
print(end - begin)
