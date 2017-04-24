import requests
import xmlrpc.client

'''
r = requests.get('http://www.pythonchallenge.com'
                 '/pc/return/disproportional.html',
                 auth=("huge", "file"))
# print(r.text)

r = requests.get('http://www.pythonchallenge.com/pc/phonebook.php',
                 auth=("huge", "file"), params={'': "Bert"})
print(r.url)
print(r.text)
'''
proxy = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com'
                                  '/pc/phonebook.php')
print(proxy.system.listMethods())
print(proxy.system.methodHelp('phone'))
print(proxy.phone('Bert'))
