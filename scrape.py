#!/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup

url = 'http://www.goheels.com/SportSelect.dbml?DB_OEM_ID=3350&SPID=12960&SPSID=668154&SITE=UNC&DB_OEM_ID=3350' # write the url here
output =""
usock = urllib2.urlopen(url)
html_data = usock.read()
usock.close()
print "Socket Opened, html_data stored and socket closed"
#print html_data

soup = BeautifulSoup(html_data)
tr_tag = soup.find_all('tr'.contents)
# type(tag)

print tr_tag

# print "Make it pretty"
# print soup

print "tag has printed"

tempData = soup.find_all('tbody.tr')
for names in tempData:
   output += names.string

output += " has worked for "

print tempData

print "tempData has printed"

tempData = soup.find_all('h4')
for companies in tempData:
    
    output += companies.string + ','

print output





