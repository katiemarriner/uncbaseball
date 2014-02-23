#!/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup

url = 'http://www.goheels.com/SportSelect.dbml?DB_OEM_ID=3350&SPID=12960&SPSID=668154&SITE=UNC&DB_OEM_ID=3350' # write the url here
output =""
usock = urllib2.urlopen(url)
html_data = usock.read()
usock.close()
print "Socket Opened, html_data stored and scoket closed"
#print html_data

soup = BeautifulSoup(html_data)

#print "Make it pretty"
#print soup

tempData = soup.find_all("odd")
for names in tempData:
    output += names.string

output += " has worked for "

print(soup.prettify())


tempData = soup.find_all('h4')
for companies in tempData:
    
    output += companies.string + ','

print output





