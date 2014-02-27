#!/usr/bin/env python

from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from roster.models import Player

import urllib2
import re

class Command(BaseCommand):
    args = '<url>'
    help = 'Parses and imports players from Goheels.com'
    
    def handle(self, *args, **options):
        try:
            print ("trying to scrape")

            response = urllib2.urlopen('http://www.goheels.com/SportSelect.dbml?DB_OEM_ID=3350&SPID=12960&SPSID=668154&SITE=UNC&DB_OEM_ID=3350')
            html = response.read()
            
            soup = BeautifulSoup(html)
            
            tabledata = soup.find("table", {"id": "roster-table"}) # find the table, the next thing to find is a table with an idea of
            player_names = []
            player_links = []
            player_position = []
            
            for link in tabledata.find_all('a'):
                player_links.append(link.get('href'))
                player_names.append(link.get('title'))
            for position in tabledata.find_all('td', {"class" : "position"}):
                player_position.append(position.text.strip())
                
            print player_names
            print player_links
            print player_position
        
        except Player.DoesNotExist:
            raise CommandError('did not work')
        
        self.stdout.write("end of scrape.py")