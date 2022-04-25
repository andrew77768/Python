import urllib.request
from bs4 import BeautifulSoup
import csv

Link_To_Scrape = [
"",
""
]

ToBin = ["","","","","","","",""]

LinksCompleted = []

LinkOutput = []

#Scrape Links from the above array Link_To_Scrape
for Link1 in Link_To_Scrape:
    ScrapePage1 = urllib.request.urlopen(Link1)
    Scrapesoup = BeautifulSoup(ScrapePage1, features="html.parser")

    for link in Scrapesoup.find_all('a'):
        LinkOutput.append(link.get('href'))

#Now we're going to remove duplicates (in a very dirty way) from LinkOutput array and put it into mylist
mylist = list(dict.fromkeys(LinkOutput))

#Now we nicen by moving it to an new array
#Don't have to do this, and could remove this and just pass the BTEC"Functions" below the mylist array instead of the LinksCompleted array
#But nah
for each in mylist:
    LinksCompleted.append(each)
#    print (each)

f = csv.writer(open("ABPScrapeExport.csv", "w")) #Open CSV in CSV Writer
f.writerow(["Name", "Email","Link"])    # Write column headers as the first line


#Hit each individual link that we took from the first
#We hit this in a try so we can escape any 404s
for Link in LinksCompleted:
#    print(Link)
    try:
        Page1 = urllib.request.urlopen(Link)
        soup = BeautifulSoup(Page1, features="html.parser")

        #Scan, Split and Drop emails before dump to the CSV
        mailtos = soup.select('a[href^=mailto]')
        name = soup.find('h1').get_text()
#        print(name)
        dropemail = 'REMOVED@EMAIL.ADDRESS' #beacuse i'm too lazy to scrape properly
        for i in mailtos:
#            print (i)
            href=i['href']
            try:
                str1, str2 = href.split(':')
            except ValueError:
                break
            if str2 == dropemail:
                pass
            else:
#                print(str2) #Added for feedback
                email = str2
        f.writerow([name, email, Link])    # Write column headers as the first line
    except:
        print ("Error404 : " + Link)
        pass
