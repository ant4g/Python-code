import urllib.request
strona = urllib.request.urlopen('strona')
print(strona.read())