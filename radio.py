#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import argparse
import os

pagina = requests.get('https://docs.google.com/spreadsheets/d/1rQncpm7tJJpHXBn1YicCYCAh0sUegDS308NZoqUqtw4/pubhtml')
soup = BeautifulSoup(pagina.text, 'html.parser')
radios = {}
table_body = soup.find('tbody')
rows = table_body.find_all('tr')
for row in rows[2:]:
	cols = row.find_all('td')
	radios[cols[1].text.strip()] = cols[2].text.strip()


parser = argparse.ArgumentParser(description="la radio que queres escuchar")
parser.add_argument("-l", "--listen", type=str, choices=radios.keys(), help="listen")
parser.add_argument("-t", "--list", action="store_true", help="lista de radios")
parser.add_argument("-a", "--add", nargs=2, help="agrega radio: nombre url")

args = parser.parse_args()
if args.listen:
	print args.listen
	os.system("cvlc %s " % radios[args.listen])
elif args.list:
	for item in radios.keys():
		print item
elif args.add:
	url = "https://docs.google.com/forms/d/e/1FAIpQLSfRqubgTMQypGMlX4JpxbCXiR6G-x8_a60zvZqb30nSzgN7xg/formResponse"
	datos = {'entry.1300081737':args.add[0], 'entry.727360622':args.add[1]}
	r = requests.post(url, datos)
	print r.status_code





