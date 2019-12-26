#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  blogspot_test.py
#  
#  Copyright 2019 Girard Aquino <girard@T500>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import requests
from bs4 import BeautifulSoup
import time

webpage = raw_input('Enter website: ') 

# Include way to check if website already in url_list.txt

with open("url_list.txt", "a") as url_list:
	url_list.write(webpage + "\n")
	print("\nAdded webpage to url_list.txt \n")

time.sleep(.5)

print("Creating soup for {}".format(webpage))
url0 = webpage
response = requests.get(url0)
soup = BeautifulSoup(response.text, 'html.parser')

time.sleep(.5)

print("\nPreparing to write file. \n")
file_name = raw_input("Enter filename (data_ADDR.txt) : ")

time.sleep(.5)

print("\nExtracting text... \n")

with open(file_name, 'w') as file:
	for text in soup.find_all('div', class_='post'):
		try:
			entry_title = text.h3.text
			#print(entry_title)
			file.write(entry_title)
		except:
			pass
		try:
			entry_body = text.find('div', class_='post-body').text
			#print(entry_body)
			#print("\n")
			file.write(entry_body)
		except:
			pass
			

	# Get links for archive; 
	archive_list = soup.find(class_="widget BlogArchive")
	archive_links = archive_list.find_all('a', class_='post-count-link') #link for the year... 
	links = []

	for a in archive_links:
		links.append(a['href'])

	# Filter archive links by year only
	links_filtered = []

	for i in links:
		if len(i) < 58: # Adapt parameter
			links_filtered.append(i)

	# Get text in archive
	for link in links_filtered:
			response = requests.get(link)
			soup = BeautifulSoup(response.text, 'html.parser')
			
			#for title in soup.find_all(class_='post-title entry-title'):
				## Get text title
				#file.write(str(title.text))
			for i in soup.find_all(class_='post-body entry-content'):
				#print(i.text)
				file.write(str(i.text.encode('utf-8')))
	
	time.sleep(2)
	print("\nSuccess...")
	time.sleep(.5)
	print("Data saved to {}".format(file_name))
	time.sleep(2)
