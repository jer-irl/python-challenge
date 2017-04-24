import requests

r = requests.get('http://www.pythonchallenge.com/pc/return/evil.html',
                 auth=("huge", "file"))
print(r.text)
