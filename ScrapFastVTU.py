import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint

response = requests.get(
    'http://cbcs.fastvturesults.com/classranks/1pe15is072/5')

links = re.compile(r"href='/student([^']*)'").findall(response.text)


studs = []
for link in links[0:]:
    try:

        myURL = "http://cbcs.fastvturesults.com/result" + link + "/5"
        response = requests.get(myURL)
        text = response.text
        soup = BeautifulSoup(text, 'html.parser')
        name = soup.select('.card-title > span:nth-of-type(1)')[0].text
        sgpa = soup.select('.card-text')[0].text
        elems = soup.find_all("div", {"class": "card-body custom-card-body"})
        stud = {}
        stud["Name"] = name
        stud["USN"] = link[1:]
        for item in elems:
            subcode = item.contents[1].find_all(
                "span", {"class": "text-muted"})[0].text.strip()
            total = float(item.contents[5].contents[7].text[6:].strip())
            point = float(item.contents[9].contents[1].text.strip()[12:])
            grade = item.contents[9].contents[3].text.strip()[12:]
            stud[subcode] = total
            stud[subcode+' Letter'] = grade
            stud[subcode+' Point'] = point

        stud["SGPA"] = float(sgpa[6:].strip())
        studs.append(stud)
        pprint(stud)
    except():
        pass

f = open('Marks.txt', 'w')
f.write(str(studs))
f.close()
