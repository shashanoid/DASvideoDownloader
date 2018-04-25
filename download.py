from bs4 import BeautifulSoup
import requests
import os
import re


url = "https://www.destroyallsoftware.com/screencasts/catalog/routing-simple-requests"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html5lib")

g_data = soup.find_all("div", {"class": "row"})

###Name text
name_data = soup.find("h2")
change_name = str(name_data.text)
############

shit = str(g_data[0].script)
split_shit = shit.split(';')

link = split_shit[5]
m = re.search(".src = (.*)\"*$", link)

download = m.group(1)
os.system("mkdir ")
##Change youtube-dl location by calling which youtube-dl
os.system('/usr/local/bin/youtube-dl -o %s.%s %s' % ('"'+change_name+'"', "mp4", download))
os.chdir("..")
os.system("mkdir newone")