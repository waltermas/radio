#!/usr/bin/python3
# formato:
#http://stream.radiotime.com/listen.stream?streamIds=63888703&rti=d09zGgJffhg4FEMbKglIXV5yHU9QXAF%2bUxVHQ19WHUhLAg1zOD1dFgEAdSwEREphXx0ZRFIVUDsLEVR2SAFYRAUVChxoGldGUxBrV1pQZAUZZBcXBggO%7e%7e%7e

import requests
import re

tuneinurl = input('ingresa tunein url: ')
#tuneinurl="http://tunein.com/radio/Super-1075-s167823/"
r = requests.get(tuneinurl)
#print(r.text)
stream = re.search(r'/stream.radiotime.com/.*?\"',  r.text)
print(stream.group())
#print(type(stream))
url2 = "http:/" + stream.group()[:-1]
print(url2)
r2 = requests.get(url2)
print(r2.text)
