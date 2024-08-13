#-*- coding: utf-8 -*-
import requests
from pprint import pprint
import xml.etree.ElementTree as ET

#url = 'https://www.tenderguru.ru/api2.3/export/contragent/inn/5003093330?dtype=json'
url = "https://www.tenderguru.ru/api2.3/export/contragent/inn/"
inn = '9710008850'
param = {"inn": inn}
headers = {'Content-Type': 'application/json'}
r_html = requests.get(url, param)
param["dtype"] = "json"


r_json = requests.get(url, param)

ll = r_json.json()[0]
inn = ll['INN']
kpp = ll['kpp']
org = ll['Org']
ogrn = ll['ogrn']
ogrn_date = ll['ogrn_date']
print(f'Организация {org}')
file = r_html.text
with open("text.txt", mode='w') as ff:
    if 'UTF-8' in file:

        new_file = file.replace('UTF-8', 'cp1251')
        new_file.encode('cp1251')
        ff.write(new_file)
    else:
        ff.write(file)

    ff.encoding.encode('cp1251')

rr = ET.XML(file)
inn = rr[0].find('INN')
kpp = rr[0].find('kpp')
org = rr[0].find('Org')
ogrn = rr[0].find('ogrn')
ogrn_date = rr[0].find('ogrn_date')
print('INN', inn.text)

et = ET.parse("text.txt")
rr = et.getroot()
inn = rr[0].find('INN')
kpp = rr[0].find('kpp')
org = rr[0].find('Org')
ogrn = rr[0].find('ogrn')
ogrn_date = rr[0].find('ogrn_date')
print('INN', inn.text)

for child in rr[0]:
    if child.tag == 'updateLink':
        print(child.attrib)
        print(child.tag, child.text)

print(r_html.url)
pprint(r_html.headers)
pprint(r_html.raise_for_status)
