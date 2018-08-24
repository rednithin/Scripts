import os
import re
import html
import requests
import unicodedata
from pprint import pprint

myRE = re.compile(r'<a href="(index.*?)">(.*?)</a>')
pdfRE = re.compile(r'"(external/.*?)"')
hostname = 'https://uva.onlinejudge.org/'

os.mkdir('UVa')
os.chdir('UVa')


def recursive(url='https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=604', count=2):
    response = requests.get(url)
    myArr = myRE.findall(response.text)[count:]
    num = 1
    if 'page=show_problem' in myArr[0][0]:
        for elem in myArr:
            response = requests.get(hostname+html.unescape(elem[0]))
            pdf = pdfRE.findall(response.text)
            name = f'{num:03}' + ' - ' + \
                re.sub(r'[\\/*?:"<>|]', "", html.unescape(elem[1]))
            response = requests.get(hostname+html.unescape(pdf[0]))
            with open(name + '.pdf', 'wb') as f:
                f.write(response.content)
            print(name)
            num += 1
        return
    for elem in myArr:
        name = f'{num:03}' + ' - ' + re.sub(r'[\\/*?:"<>|]', "", elem[1])
        os.mkdir(name)
        os.chdir(name)
        print(name)
        recursive(url=hostname+html.unescape(elem[0]), count=count+1)
        os.chdir('..')
        num += 1


recursive()
