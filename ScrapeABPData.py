import urllib.request
from bs4 import BeautifulSoup
import csv

Links = [
"Fake.Site",
"Fake.Site",
"Fake.Site"
]

f = csv.writer(open("ABPScrapeExport.csv", "w")) #Open CSV in CSV Writer
f.writerow(["Name", "Email","Link"])    # Write column headers as the first line

for Link in Links:
    print(Link)
    Page1 = urllib.request.urlopen(Link)
    soup = BeautifulSoup(Page1, features="html.parser")

    #Scan, Split and Drop emails before dump
    mailtos = soup.select('a[href^=mailto]')
    name = soup.find('h1').get_text()
    print(name)
    dropemail = 'Drop@This.Mail'
    for i in mailtos:
        href=i['href']
        try:
            str1, str2 = href.split(':')
        except ValueError:
            break
        if str2 == dropemail:
            pass
        else:
            print(str2) #Added for feedback
            email = str2
    f.writerow([name, email, Link])    # Write column headers as the first line
