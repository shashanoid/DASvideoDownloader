from bs4 import BeautifulSoup
import requests
import os
import re

url = "https://www.destroyallsoftware.com/screencasts/catalog/"
r = requests.get(url)

start_url = "https://www.destroyallsoftware.com"

soup = BeautifulSoup(r.content, "html5lib")

g_data = soup.find_all("div", {"class" : "episodes"})
folder_data = soup.find_all("h1")

folder_names = []

for i in xrange(1,9):
	folder_names.append(folder_data[i].img['alt'])

divs = []
for links in g_data:
	divs.append(links)

#Links to download videos from
scrape_links = []

for div in divs:
	new_soup = div.find_all("a")
	for links in new_soup:
		scrape_links.append(start_url + links['href'])


###################################################################
#Video download
os.system("mkdir videos")
os.chdir("videos")
###################################################################



for x in xrange(1,8):
	os.system("mkdir %s" % folder_names[x])
	os.chdir("")
	# os.system("")
	os.chdir("..")